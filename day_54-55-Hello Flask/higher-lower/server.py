from flask import Flask
from random import randint
app = Flask(__name__)

number = randint(0,9)
@app.route("/")
def home():
    return '<h1 style="text-align: center">Guess a number between 0 and 9!</h1>'\
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200>'


@app.route("/<int:guess>")
def check_guess(guess):
    if guess > number:
        return '<h1 style="text-align: center color: red">Your guess is too high!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=200>'
    elif guess < number:
        return '<h1 style="text-align: center color: blue">Your guess is too low!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=200>'
    else:
        return '<h1 style="text-align: center color: orange">You found me!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=200>'



if __name__ == "__main__":
    app.run(debug=True)