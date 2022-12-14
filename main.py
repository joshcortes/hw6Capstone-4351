
from typing import ItemsView
from urllib import request
import requests
import os
from flask_sqlalchemy import SQLAlchemy
import flask
import json
app = flask.Flask(__name__)
BOOKS = ["The Maze Runner", "Harry Potter and The Sorcerer's Stone",
         "Goosebumps and Welcome to Horror Land", "Holes", "The Alchemyst and The Secrets of the Immortal Nicholas Flamel"]
basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + \
    os.path.join(basedir, 'database.db')
# Gets rid of a warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    subtitle = db.Column(db.String(80))
    thumbnail = db.Column(db.String(120))
    author = db.Column(db.String(80))


with app.app_context():
    db.create_all()


@app.route("/delete", methods=["POST"])
def delete():
    description_to_delete = json.loads(flask.request.data.decode())
    to_delete = Upload.query.filter_by(title=description_to_delete).first()
    db.session.delete(to_delete)
    db.session.commit()
    return flask.redirect("/")


@app.route('/', methods=["GET", "POST"])  # Python decorator
def index():
    book_data = flask.request.args
    query = book_data.get("title")
    newbooks = []
    newthumbnails = []
    if query is not None:
        newbooks = get_book(query)

    if flask.request.method == "POST":
        data = flask.request.form
        new_upload = Upload(title=data["title"])
        db.session.add(new_upload)
        db.session.commit()

    uploads = Upload.query.all()
    num_uploads = len(uploads)
    return flask.render_template("index.html",
                                 length=len(BOOKS),
                                 books=title,
                                 images=thumbnail,
                                 newbooks=newbooks,
                                 newthumbnails=newthumbnails, num_uploads=num_uploads,
                                 uploads=uploads,

                                 )


API_KEY = "AIzaSyDNWM1nYm-SZPUhpCCd5Ovn0Zlyw_EGyjQ"


bookz_list = ["The Maze Runner", "Harry Potter and The Sorcerer's Stone",
              "Goosebumps and Welcome to Horror Land", "Holes", "The Alchemyst and The Secrets of the Immortal Nicholas Flamel"]
title = []
thumbnail = []
for query in bookz_list:
    response = requests.get("https://www.googleapis.com/books/v1/volumes",
                            params={"q": query, "key": API_KEY})
    response_json = response.json()
    title.append(response_json["items"][0]
                 ["volumeInfo"]["title"])
    thumbnail.append(response_json["items"][0]["volumeInfo"]
                     ["imageLinks"]["thumbnail"])
    bookz_list = ["The Maze Runner", "Harry Potter and The Sorcerer's Stone",
                  "Goosebumps and Welcome to Horror Land", "Holes", "The Alchemyst and The Secrets of the Immortal Nicholas Flamel"]


def get_book(query):
    response = requests.get("https://www.googleapis.com/books/v1/volumes",
                            params={"q": query, "key": API_KEY})
    response_json = response.json()
    newbooks = []
    newthumbnails = []

    for query in response_json["items"][:1]:
        newbooks.append(query["volumeInfo"]["title"])
        newthumbnails.append(query["volumeInfo"]
                             ["imageLinks"]["thumbnail"])

    return newbooks, newthumbnails


app.run()
