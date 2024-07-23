from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests



API_KEY = "40d5365897e6c20cff5f4841a54c0f7e"
TMDB_EP = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"
FIND_MOVIE_EP = "https://api.themoviedb.org/3/movie"
url = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"


headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MGQ1MzY1ODk3ZTZjMjBjZmY1ZjQ4NDFhNTRjMGY3ZSIs"
                     "Im5iZiI6MTcyMTc0NTY4Mi40NjYwNzIsInN1YiI6IjY2OWZiZWNhYzgxZTlmMGRhNzZlN2Q3MyIsInNjb3Bl"
                     "cyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.6oJKa865ltDEv49pHewd275t5kybK5-N7emjvRh3mBE"
    }



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

##CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///top10-movies.db"

# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)


##CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=False, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=True)

with app.app_context():
    db.create_all()

# #Add first new movie manually
#     new_movie = Movie(
#         title="Phone Booth",
#         year=2002,
#         description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#         rating=7.3,
#         ranking=10,
#         review="My favourite character was the caller.",
#         img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
#     db.session.add(new_movie)
#     db.session.commit()
#
# # 2nd new movie manually
#     second_movie = Movie(
#         title="Avatar The Way of Water",
#         year=2022,
#         description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#         rating=7.3,
#         ranking=9,
#         review="I liked the water.",
#         img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#     )
#     db.session.add(second_movie)
#     db.session.commit()

class EditForm(FlaskForm):
    new_rating = StringField(label='Your Rating Out of 10 e.g. 7.5')
    new_review = StringField(label='Your Review')
    submit = SubmitField(label='Done')

class FindMovieForm(FlaskForm):
    movie_title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Search Movie")
@app.route("/")
def home():
    ##READ ALL RECORDS
    # Construct a query to select from the database. Returns the rows in the database
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    # Use .scalars() to get the elements rather than entire rows from the database
    all_movies = result.scalars().all()[::-1]
    # This line loops through all the movies
    for i in range(len(all_movies)):
        # This line gives each movie a new ranking in ascending order from their order in all_movies
        all_movies[i].ranking = i + 1
    db.session.commit()
    return render_template("index.html", movies=all_movies)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = FindMovieForm()
    if form.validate_on_submit():
        parameters = {
            "query": form.movie_title.data,
            "include_adult": "false",
            "language": "en-US",
            "page": "1",
        }
        response = requests.get(TMDB_EP, headers=headers, params=parameters)
        response.raise_for_status()
        movie_data = response.json()
        return render_template('select.html', movies=movie_data)
    return render_template('add.html', form=form)

# @app.route('/select', methods=['GET', 'POST'])
# def select():
#     return render_template('select.html', movie=movie_data)
@app.route('/edit', methods=['GET', 'POST'])
def edit():
    form = EditForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        if form.new_rating.data:
            movie.rating = form.new_rating.data
        if form.new_review.data:
            movie.review = form.new_review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie, form=form)

@app.route('/find_movie', methods=['GET', 'POST'])
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        parameters2 = {
            "language": "en-US",
        }
        response = requests.get(f"{FIND_MOVIE_EP}/{movie_api_id}", headers=headers, params=parameters2)
        response.raise_for_status()
        movie_data = response.json()

        #Add new movie to db
        new_movie = Movie(
            title=movie_data['title'],
            year=movie_data['release_date'],
            description=movie_data['overview'],
            img_url=f"{MOVIE_DB_IMAGE_URL}/{movie_data['poster_path']}"
        )
        db.session.add(new_movie)
        db.session.commit()
    # Redirect to /edit route
    return redirect(url_for("edit", id=new_movie.id))

@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    # Delete RECORD
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
