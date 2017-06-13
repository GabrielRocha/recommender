from Code.movielens.movielens import get_movies, get_reviews


def test_get_movies():
    movies = get_movies()
    assert movies.get("1") == "Toy Story (1995)"


def test_get_reviews():
    reviews = get_reviews()
    assert "242" in reviews.get("196")
    assert reviews.get("196")["242"] == 3.0
