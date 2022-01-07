from flask import Flask, request, render_template, jsonify
from functions import get_all_movie_by_title, get_all_movie_between_years, get_all_movie_by_rating, \
    get_all_movie_by_genre, get_actors_company, filter_movies

app = Flask(__name__)


@app.route('/movies/<title>')
def page_movies_by_title(title):
    movie = get_all_movie_by_title(title)

    return jsonify(movie)


@app.route('/years/<int:year_from>/to/<int:year_to>')
def page_movies_between_years(year_from, year_to):
    movie = get_all_movie_between_years(year_from, year_to)

    return jsonify(movie)


@app.route('/rating/children/')
def rating_children():
    movie = get_all_movie_by_rating(['G'])
    return jsonify(movie)


@app.route('/rating/family/')
def rating_family():
    movie = get_all_movie_by_rating(['PG', 'PG-13'])
    return jsonify(movie)


@app.route('/rating/adult/')
def rating_adult():
    movie = get_all_movie_by_rating(['R', 'NC-17'])
    return jsonify(movie)


@app.route('/genre/<movie_genre>')
def page_movie_by_genre(movie_genre):
    movie = get_all_movie_by_genre(movie_genre)

    return jsonify(movie)


@app.route('/actors/<first_actor>/and/<second_actor>')
def page_actors_company(first_actor, second_actor):
    movie = get_actors_company(first_actor, second_actor)

    return jsonify(movie)


@app.route('/search/<movie_type>/<int:year>/<genre_type>')
def page_search_movie_by_filter(movie_type, year, genre_type):
    movie = filter_movies(movie_type, year, genre_type)

    return jsonify(movie)


app.run()
