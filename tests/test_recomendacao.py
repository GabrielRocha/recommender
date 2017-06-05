from Code.recomendacao import Recomendacao
import pytest
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def base():
    return Recomendacao(BASE_DIR+"/base.txt")


@pytest.mark.parametrize("user", [('user_a', 0.07),
                                  ('user_b', 0.04)])
def test_get_similares(base, user):
    assert user in base.get_similares('user_c').items()


@pytest.mark.parametrize("user", ["user_a", "user_b", "user_c"])
def test_list_all_users(base, user):
    assert user in base.all_users()


def test_more_similar(base):
    user_similar, distance = base.more_similar('user_a')
    assert user_similar == "user_c"
    assert distance, 13.45


@pytest.mark.parametrize("movie",["a", "b", "c", "d", "e"])
def test_get_all_movieis_available(base, movie):
    assert movie in base.get_all_movieis_available()


def test_get_all_movieis_available(base):
    assert len(base.get_all_movieis_available()) == 5


def test_movies_not_seen(base):
    assert "c" and "e" in base.movies_not_seen("user_c")


@pytest.mark.parametrize("movie", ["c", "e"])
def test_who_saw_movie_not_seen(base, movie):
    assert "user_a" and "user_b" in base.who_saw_movie_not_seen("user_c")[movie]
