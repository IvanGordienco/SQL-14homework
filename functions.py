import json
import sqlite3


def get_all_movie_by_title(title):
    #  поиск по названию.
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


def get_all_movie_between_years(year1, year2):
    # поиск по диапазону лет выпуска с лимитом в 100 тайтл.
    con = sqlite3.connect("netflix.db")

    sqlite_query = "SELECT `title`,`country`,`release_year`,`listed_in`,`description` " \
                   "FROM netflix " \
                   f"WHERE release_year BETWEEN {year1} AND {year2} " \
                   "ORDER BY release_year DESC " \
                   "LIMIT 100"

    cur = con.cursor()
    cur = cur.execute(sqlite_query)
    data = []

    for row in cur.fetchall():
        movie = {
            "Title": row[0],
            "Country": row[1],
            "Release_year": row[2],
            "Genre": row[3],
            "Description": row[4]

        }
        data.append(movie)
    con.close()
    return data


def get_all_movie_by_rating(rating):
    # поиск по рейтингу,Определение группы: для детей, для семейного просмотра, для взрослых.
    con = sqlite3.connect("netflix.db")

    sqlite_query = \
        "SELECT `title`, `rating`, `description` " \
        "FROM netflix " \
        f"WHERE `rating` IN ('{rating}') " \
        "LIMIT 100 "

    cur = con.cursor()
    cur = cur.execute(sqlite_query)
    data = []

    for row in cur.fetchall():
        movie_by_rating = {
            "Title": row[0],
            "Rating": row[1],
            "Description": row[2]

        }
        data.append(movie_by_rating)
    con.close()
    return data


def get_all_movie_by_genre(genre):
    # функция, которая получает название жанра в качестве аргумента и
    # возвращает 10 самых свежих фильмов

    con = sqlite3.connect("netflix.db")
    genre = genre.lower()
    sqlite_query = \
        "SELECT `title`, `description`, `listed_in` " \
        "FROM netflix " \
        f"WHERE `listed_in` LIKE '%{genre}%' " \
        "LIMIT 10 " \
        # "ORDER BY DESC " \ - Почему-то не хочет работать

    cur = con.cursor()
    cur = cur.execute(sqlite_query)
    data = []

    for row in cur.fetchall():
        movie_by_genre = {
            "Title": row[0],
            "Description": row[1],
            "Listed_in": row[2]

        }
        data.append(movie_by_genre)
    con.close()
    return data


def get_actors_company(first_actor, second_actor):
    #  функция, которая получает в качестве аргумента имена двух актеров,
    # сохраняет всех актеров из колонки cast и возвращает список тех, кто играет с ними в паре больше 2 раз

    con = sqlite3.connect("netflix.db")

    sqlite_query = \
        "SELECT GROUP_CONCAT(`cast`, ','), `title`  " \
        "FROM netflix " \
        f"WHERE `cast` LIKE '%{first_actor}%' AND `cast` LIKE '%{second_actor}%' "

    cur = con.cursor()
    cur = cur.execute(sqlite_query)
    data_raw = cur.fetchone()
    data = []

    actors_list = data_raw[0].split(", ")
    actors_list_unique = set(actors_list)

    actors_list_unique.remove(first_actor)
    actors_list_unique.remove(second_actor)
    data.append(actors_list_unique)

    return data


def filter_movies(movie_type, year, genre):
    # фунция, с помощью которой можно будет передавать тип картины (фильм или сериал),
    # год выпуска и ее жанр в БД

    con = sqlite3.connect("netflix.db")

    sqlite_query = \
        "SELECT `title`, `description`, `listed_in`, `release_year` " \
        "FROM netflix " \
        f"WHERE `type` = '{movie_type}' AND `release_year` = {year} AND  `listed_in` LIKE '%{genre}%' " \
        "LIMIT 100 "

    cur = con.cursor()
    cur = cur.execute(sqlite_query)
    data = []

    for row in cur.fetchall():
        movie_by_rating = {
            "Title": row[0],
            "Description": row[1],
            "Listed_in": row[2],
            "Release_year": row[3]

        }
        data.append(movie_by_rating)
    con.close()
    return data
