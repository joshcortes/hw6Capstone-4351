
from typing import ItemsView
from urllib import request
import requests

import flask
import json
app = flask.Flask(__name__)
BOOKS = ["The Maze Runner", "Harry Potter and The Sorcerer's Stone",
         "Goosebumps and Welcome to Horror Land", "Holes", "The Alchemyst and The Secrets of the Immortal Nicholas Flamel"]
# IMAGES = [
#     "/static/maze.png",
#     "/static/harrypotter.jpg",
#     "/static/goosebumps.jpg",
#     "/static/holes.png",
#     "/static/alchemyst.jpg"
# ]


@app.route('/', methods=['GET'])  # Python decorator
def index():
    book_data = flask.request.args
    query = book_data.get("title")
    newbooks = []
    newthumbnails = []
    if query is not None:
        newbooks = get_book(query)

    return flask.render_template("index.html",
                                 length=len(BOOKS),
                                 books=title,
                                 images=thumbnail,
                                 newbooks=newbooks,
                                 newthumbnails=newthumbnails

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

        for query in response_json["items"][:1]:
            newthumbnails.append(query["volumeInfo"]
                                 ["imageLinks"]["thumbnail"])

    return newbooks, newthumbnails


app.run()
