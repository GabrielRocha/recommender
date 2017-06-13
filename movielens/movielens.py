import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def dict_movies():
    movie = {}
    for row in open(BASE_DIR+"/data/u.item"):
        id, title = row.split("|")[0:2]
        movie[id] = title
    return movie
