
import flask
app = flask.Flask(__name__)
BOOKS = ["Maze Runner", "Harry Potter",
         "Goosebumps", "Holes", "The Alchemyst"]
IMAGES = [
    "/static/maze.png",
    "/static/harrypotter.jpg",
    "/static/goosebumps.jpg",
    "/static/holes.png",
    "/static/alchemyst.jpg"

]


@app.route('/')  # Python decorator
def index():

    return flask.render_template("index.html",
                                 length=len(BOOKS),
                                 books=BOOKS,
                                 images=IMAGES,
                                 )


app.run()
