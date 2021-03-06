import os
from flask import (
    Flask, render_template, redirect, url_for, flash, request, session)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists('env.py'):
    import env


app = Flask(__name__)

app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
@app.route('/book_review_club')
def book_review_club():
    """
        Render home page with available books and quotes from db
    """

    books = list(mongo.db.books.find())
    copyright_year = datetime.datetime.now().strftime("%Y")
    quotes = list(mongo.db.quotes.find())
    return render_template(
        "index.html", books=books, copyright_year=copyright_year,
        quotes=quotes)


@app.route('/search', methods=['GET', 'POST'])
def search():
    """
        Search books within title and description section
    """

    query = request.form.get('search')
    books = list(mongo.db.books.find({"$text": {"$search": query}}))
    copyright_year = datetime.datetime.now().strftime("%Y")
    return render_template(
        "search.html", books=books, copyright_year=copyright_year)


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    """
        Sign up function
    """

    if request.method == "POST":

        existing_username = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_username:
            flash("Username already exists")
            return redirect(url_for('sign_up'))

        sign_up = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }

        mongo.db.users.insert_one(sign_up)
        session["user"] = request.form.get("username").lower()
        return redirect(url_for('profile', username=session["user"]))

    return render_template("sign_up.html")


@app.route('/term_and_conditions')
def term_and_conditions():
    """
        Render term and condition section
    """

    return render_template("term_and_conditions.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    """
        Log in function
    """

    if request.method == "POST":
        # check user in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # check if user exist
        if existing_user:
            # check passowrd
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for('profile', username=session["user"]))
            else:
                flash("Incorect Username and/or Password")
                return redirect(url_for('login'))
        else:
            flash("Incorect Username and/or Password")
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/profile/<username>')
def profile(username):
    """
        render user profile from db
    """

    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for('login'))


@app.route('/book_collection/<book_id>', methods=["GET", "POST"])
def book_collection(book_id):
    """
        render my book collection from db
        user can like/unlike the book, write a review
        user can delete its own review.
        admin can delete all reviews.
    """

    # redirect to login page if there is no login user
    if session.get("user") is None:
        flash("Please login first")
        return redirect(url_for('login'))

    # make heart active if user liked the book already
    checkbox = []
    tooltip_value = 'Love it'
    if mongo.db.books.count_documents(
            {"_id": ObjectId(book_id), "liked_by":
             {"$elemMatch": {"_user": session["user"]}}}) != 0:
        checkbox = 'checked'
        tooltip_value = 'Not a Fan'

    # review post
    if request.method == "POST":
        if request.form.get("btn") == "submit":
            submit = {
                "review_by": session["user"],
                "review_date": datetime.datetime.now().strftime(
                    "%b %d %Y %H:%M:%S"),
                "review_date_value": int(
                    datetime.datetime.now().strftime('%Y%m%d%H%M%S')),
                "reviw_description": request.form.get("review_description"),
                "review_id": ObjectId()
            }

            mongo.db.books.update_one({"_id": ObjectId(book_id)}, {
                "$push": {"book_review": submit}})
    # like post
        else:
            if mongo.db.books.count_documents(
                    {"_id": ObjectId(book_id),
                     "liked_by": {"$elemMatch":
                                  {"_user": session["user"]}}}) != 0:
                mongo.db.books.update_one(
                    {"_id": ObjectId(book_id)},
                    {"$pull": {"liked_by": {"_user": session["user"]}}})
                checkbox = []
                tooltip_value = 'Love it'
            else:
                mongo.db.books.update_one(
                    {"_id": ObjectId(book_id)},
                    {"$push": {"liked_by": {"_user": session["user"]}}})
                checkbox = 'checked'
                tooltip_value = 'Not a Fan'

    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template(
        "book_collection.html",
        book=book, checkbox=checkbox, tooltip_value=tooltip_value)


@app.route('/delete_review/<book_id>/<review_item>')
def delete_review(book_id, review_item):
    """
        Delete review function
    """
    mongo.db.books.update_one(
        {"_id": ObjectId(book_id)},
        {"$pull": {"book_review": {"review_id": ObjectId(review_item)}}})

    return redirect(url_for('book_collection', book_id=book_id))


@app.route("/book_collection", methods=["GET", "POST"])
def add_book_collection():
    """
        add book collection function. user can add book to db.
        user needs to log in first.
    """

    # redirect to login page if there is no login user
    if session.get("user") is None:
        flash("Please login first")
        return redirect(url_for('login'))

    if request.method == "POST":
        display_title = request.form.get('book_title').title()
        if len(display_title) > 20:
            display_title = display_title[:20] + '...'

        book = {
            "book_image_url": request.form.get("book_image_url"),
            "book_author": request.form.get("book_author").title(),
            "book_title": request.form.get("book_title"),
            "book_display_title": display_title,
            "book_description": request.form.get("book_description"),
            "added_by": session["user"]
        }
        mongo.db.books.insert_one(book)
        flash("successfully added to your collection")

    # m_admin can delete or edit all books but users can just modify theirs
    if session["user"] == "m_admin":
        books = list(mongo.db.books.find())
    else:
        books = list(mongo.db.books.find({"added_by": session["user"]}))

    return render_template("add_book_collection.html", books=books)


@app.route("/edit_book_collection/<book_id>", methods=["GET", "POST"])
def edit_book_collection(book_id):
    """
        edit books in the book collection section
    """
    # redirect to login page if there is no logged in user
    if session.get("user") is None:
        flash("Please login first")
        return redirect(url_for('login'))

    # Prohibit if a user try to edit another user book (except admin user)
    if session.get("user") != mongo.db.books.find_one(
        {"_id": ObjectId(book_id)})["added_by"] and session.get(
            "user") != "m_admin":
        flash("You do not have permission to edit this book")
        return redirect(url_for('login'))

    edit_book = mongo.db.books.find({"_id": ObjectId(book_id)})

    if request.method == "POST":
        display_title = request.form.get('book_title').title()
        if len(display_title) > 20:
            display_title = display_title[:20] + '...'

        book = {
            "book_image_url": request.form.get("book_image_url"),
            "book_author": request.form.get("book_author").title(),
            "book_title": request.form.get("book_title"),
            "book_display_title": display_title,
            "book_description": request.form.get("book_description"),
            "added_by": session["user"],
        }

        mongo.db.books.update_one({"_id": ObjectId(book_id)}, {"$set": book})
        flash("successfully updated")

    return render_template("edit_book_collection.html", edit_book=edit_book)


@app.route("/delete_book_collection/<book_id>", methods=["GET", "POST"])
def delete_book_collection(book_id):
    """
        Delete books in book collection section
    """
    # redirect to login page if there is no logged in user
    if session.get("user") is None:
        flash("Please login first")
        return redirect(url_for('login'))

    # Prohibit if a user try to delete another user book (except admin user)
    if session.get("user") != mongo.db.books.find_one(
        {"_id": ObjectId(book_id)})["added_by"] and session.get(
            "user") != "m_admin":
        flash("You do not have permission to delete this book")
        return redirect(url_for('login'))

    mongo.db.books.remove(
        {"_id": ObjectId(book_id)})
    flash("successfully deleted")

    books = list(mongo.db.books.find({"added_by": session["user"]}))
    return render_template("add_book_collection.html", books=books)


@app.route('/logout')
def logout():
    """
        Log out function
    """

    session.pop("user")
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'), port=int(
        os.environ.get('PORT')), debug=False)
