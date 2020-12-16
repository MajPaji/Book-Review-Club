import os
from flask import (
    Flask, render_template, redirect, url_for, flash, request, session)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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

    return render_template("sign_up.html")


@app.route('/term_and_conditions')
def term_and_conditions():
    return render_template("term_and_conditions.html")


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'), port=int(
        os.environ.get('PORT')), debug=True)
