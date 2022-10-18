
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


@app.route('/')  # Python decorator
def index():

    return flask.render_template("index.html",
                                 length=len(BOOKS),
                                 books=title,
                                 images=thumbnail,
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


app.run()
