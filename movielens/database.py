from collections import Counter
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_movies():
    movie = {}
    for row in open(BASE_DIR+"/data/u.item"):
        id, title = row.split("|")[0:2]
        movie[id] = title
    return movie


def get_reviews():
    movies = get_movies()
    reviews = {}
    for row in open(BASE_DIR+"/data/u.data"):
        user, id_movie, review = row.split("\t")[0:3]
        reviews.setdefault(user, {})
        reviews[user][movies[id_movie]] = float(review)
    return reviews


def duplicates_movies():
    count_title = Counter(get_movies().values())
    return (title for title in count_title if count_title[title] > 1)

