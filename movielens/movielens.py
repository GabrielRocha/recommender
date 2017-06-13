import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_movies():
    movie = {}
    for row in open(BASE_DIR+"/data/u.item"):
        id, title = row.split("|")[0:2]
        movie[id] = title
    return movie


def get_reviews():
    reviews = {}
    for row in open(BASE_DIR+"/data/u.data"):
        user, id_movie, review = row.split("\t")[0:3]
        reviews.setdefault(user, {})
        reviews[user][id_movie] = float(review)
    return reviews

