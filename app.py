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
    books = list(mongo.db.books.find())
    return render_template("index.html", books=books)


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():

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
    return render_template("term_and_conditions.html")


@app.route('/login', methods=["GET", "POST"])
def login():

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
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for('login'))


@app.route('/book_collection/<book_id>', methods=["GET", "POST"])
def book_collection(book_id):

    if session.get("user") is None:
        flash("Please login first")
        return redirect(url_for('login'))

    checkbox = []
    tooltip_value = 'Love it'
    if mongo.db.books.find({"_id": ObjectId(book_id), "liked_by": {"$elemMatch": {"_user": session["user"]}}}).count() != 0:
        checkbox = 'checked'
        tooltip_value = 'Love it'

    if request.method == "POST":
        if request.form.get("btn") == "submit":
            submit = {
                "review_by": session["user"],
                "review_date": datetime.datetime.now().strftime("%b %d %Y %H:%M:%S"),
                "review_date_value": int(datetime.datetime.now().strftime('%Y%m%d%H%M%S')),
                "reviw_description": request.form.get("review_description"),
                "review_id": ObjectId()
            }

            mongo.db.books.update({"_id": ObjectId(book_id)}, {
                "$push": {"book_review": submit}})
        else:

            if mongo.db.books.find({"_id": ObjectId(book_id), "liked_by": {"$elemMatch": {"_user": session["user"]}}}).count() != 0:
                print('hello')
                print(mongo.db.books.find({"_id": ObjectId(book_id)}, {
                      "liked_by": {"$elemMatch": {"_user": session["user"]}}}).count())
                mongo.db.books.update({"_id": ObjectId(book_id)}, {
                                      "$pull": {"liked_by": {"_user": session["user"]}}})
                checkbox = []
                tooltip_value = 'Love it'
            else:
                print('2')
                print(mongo.db.books.find({"_id": ObjectId(book_id), "liked_by": {
                      "$elemMatch": {"_user": session["user"]}}}).count())
                mongo.db.books.update({"_id": ObjectId(book_id)}, {
                                      "$push": {"liked_by": {"_user": session["user"]}}})
                checkbox = 'checked'
                tooltip_value = 'Not a Fan'

    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template("book_collection.html", book=book, checkbox=checkbox, tooltip_value=tooltip_value)


@app.route('/delete_review/<book_id>/<review_item>')
def delete_review(book_id, review_item):
    mongo.db.books.update({"_id": ObjectId(book_id)}, {
                          "$pull": {"book_review": {"review_id": ObjectId(review_item)}}})

    return redirect(url_for('book_collection', book_id=book_id))


@app.route('/logout')
def logout():

    session.pop("user")
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'), port=int(
        os.environ.get('PORT')), debug=True)
