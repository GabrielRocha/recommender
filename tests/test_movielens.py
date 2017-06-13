from Code.movielens.movielens import dict_movies


def test_from_movielens():
    movies = dict_movies()
    assert movies.get("1") == "Toy Story (1995)"
