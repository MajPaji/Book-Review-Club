import os
from flask import (
    Flask, render_template, redirect, url_for, flash, request, session)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'), port=int(
        os.environ.get('PORT')), debug=True)
