from Code.movielens.database import get_movies, get_reviews, duplicates_movies
import pytest


def test_get_movies():
    movies = get_movies()
    assert movies.get("1") == "Toy Story (1995)"
    assert len(movies) == 1682


def test_get_reviews():
    reviews = get_reviews()
    assert 'Ace Ventura: Pet Detective (1994)' in reviews.get("196")
    assert reviews.get("196")['Ace Ventura: Pet Detective (1994)'] == 5.0
    assert len(reviews) == 943


@pytest.mark.parametrize("movie", ['Hurricane Streets (1998)',
                                   'Fly Away Home (1996)',
                                   'That Darn Cat! (1997)'])
def test_duplicates_movies(movie):
    assert movie in duplicates_movies()
