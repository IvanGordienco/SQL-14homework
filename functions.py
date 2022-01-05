import json
import sqlite3
import pprint


def get_all_movie_by_title(title):
    con = sqlite3.connect("netflix.db")

    sqlite_query = "SELECT `title`,`country`,`release_year`,`listed_in`,`description` " \
                   "FROM netflix " \
                   f"WHERE title = '{title}' " \
                   "ORDER BY `release_year` " \
                   "LIMIT 1"

    cur = con.cursor()
    cur = cur.execute(sqlite_query)
    data_raw = cur.fetchone()
    data = {
        "Title": data_raw[0],
        "Country": data_raw[1],
        "Release_year": data_raw[2],
        "Genre": data_raw[3],
        "Description": data_raw[4]

    }
    con.close()
    return data


# pprint.pprint(get_all_movie_by_title("A Monster Calls"))


def get_all_movie_between_years(year1, year2):
    con = sqlite3.connect("netflix.db")

    sqlite_query = "SELECT `title`,`country`,`release_year`,`listed_in`,`description` " \
                   "FROM netflix " \
                   f"WHERE release_year BETWEEN {year1} AND {year2} " \
                   "ORDER BY release_year DESC " \
                   "LIMIT 100"

    cur = con.cursor()
    cur = cur.execute(sqlite_query)
    data_raw = cur.fetchone()
    data = []

    for row in cur.fetchall():
        movie = {
            "Title": data_raw[0],
            "Country": data_raw[1],
            "Release_year": data_raw[2],
            "Genre": data_raw[3],
            "Description": data_raw[4]

        }
        data.append(movie)
    con.close()
    return data


# pprint.pprint(get_all_movie_between_years(2015, 2021))

def get_all_movie_by_rating(rating):
    con = sqlite3.connect("netflix.db")

    sqlite_query = \
        "SELECT `title`, `rating`, `description` " \
        "FROM netflix " \
        f"WHERE `rating` IN ('{rating}') " \
        "LIMIT 100 "

    cur = con.cursor()
    cur = cur.execute(sqlite_query)
    data_raw = cur.fetchone()
    data = []

    for row in cur.fetchall():
        movie_by_rating = {
            "Title": data_raw[0],
            "Rating": data_raw[1],
            "Description": data_raw[2]

        }
        data.append(movie_by_rating)
    con.close()
    return data


# pprint.pprint(get_all_movie_by_rating("PG"))


def get_all_movie_by_genre(genre):
    con = sqlite3.connect("netflix.db")

    sqlite_query = \
        "SELECT `title`, `description`, `listed_in` " \
        "FROM netflix " \
        f"WHERE `listed_in` LIKE '%{genre}%' " \
        "LIMIT 10 " \
        "ORDER BY DESC "

    cur = con.cursor()
    cur = cur.execute(sqlite_query)
    data_raw = cur.fetchone()
    data = []

    for row in cur.fetchall():
        movie_by_rating = {
            "Title": data_raw[0],
            "Description": data_raw[1],
            "Listed_in": data_raw[2]

        }
        data.append(movie_by_rating)
    con.close()
    return data


# pprint.pprint(get_all_movie_by_genre("Thrillers"))

def get_actors_company(first_actor, second_actor):
    con = sqlite3.connect("netflix.db")

    sqlite_query = \
        "SELECT GROUP_CONCAT(`cast`, ','), `title`  " \
        "FROM netflix " \
        f"WHERE `cast` LIKE '%{first_actor}%' AND `cast` LIKE '%{second_actor}%' "

    cur = con.cursor()
    cur = cur.execute(sqlite_query)
    data_raw = cur.fetchone()

    actors_list = data_raw[0].split(", ")
    actors_list_unique = set(actors_list)

    actors_list_unique.remove(first_actor)
    actors_list_unique.remove(second_actor)
    return actors_list_unique


# pprint.pprint(get_actors_company("Rose McIver","Ben Lamb"))

def filter_movies(movie_type, year, genre):
    con = sqlite3.connect("netflix.db")

    sqlite_query = \
        "SELECT `title`, `description`, `listed_in`, `release_year` " \
        "FROM netflix " \
        f"WHERE `type` = '{movie_type}' AND `release_year` = {year} AND  `listed_in` LIKE '%{genre}%' " \
        "LIMIT 100 "

    cur = con.cursor()
    cur = cur.execute(sqlite_query)
    data_raw = cur.fetchone()
    data = []

    for row in cur.fetchall():
        movie_by_rating = {
            "Title": data_raw[0],
            "Description": data_raw[1],
            "Listed_in": data_raw[2],
            "Release_year": data_raw[3]

        }
        data.append(movie_by_rating)
    con.close()
    return data
# pprint.pprint(filter_movies("Movie", "2010", "Stand-Up Comedy"))
