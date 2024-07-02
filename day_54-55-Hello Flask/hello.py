from flask import Flask
# from functools import wraps
app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>'\
           '<p>This is a paragraph</p>'\
            '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmV6ZTVjY3owZGwzOGUyZWl'\
             'ubHhldWo2Yzlpa2h0ZnBiOHd5amdtMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oriO0'\
             'OEd9QIDdllqo/giphy.gif" width=200>'


def make_bold(function):
    def wrap():
        return f"<b>{function()}</b>"
    return wrap


def make_italic(function):
    def wrap():
        return f"<em>{function()}</em>"
    return wrap


def make_underlined(function):
    def wrap():
        return f"<u>{function()}</u>"
    return wrap


@app.route("/bye")
@make_bold
@make_italic
@make_underlined
def bye():
    return "Bye!"

@app.route("/username/<name>/<int:number>")
def greet(name):
    return f"Hello {name}, you are {number}"

if __name__ == "__main__":
    app.run(debug=True)