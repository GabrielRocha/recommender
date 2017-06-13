from movielens.database import get_reviews
from recommender import Analysis, from_json, from_movielens
import pytest
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def analysis():
    return from_json(BASE_DIR+"/base.txt")


def test_from_json():
    assert isinstance(from_json(BASE_DIR+"/base.txt"), Analysis)
    assert json.loads(json.dumps(from_json(BASE_DIR+"/base.txt").base))


@pytest.mark.parametrize("user", [('user_a', 0.07),
                                  ('user_b', 0.04)])
def test_get_similares(analysis, user):
    assert user in analysis.get_similares('user_c')


@pytest.mark.parametrize("user", ["user_a", "user_b", "user_c"])
def test_list_all_users(analysis, user):
    assert user in analysis.all_users()


def test_more_similar(analysis):
    user_similar, distance = analysis.more_similar('user_a')
    print(user_similar, distance)
    assert user_similar == "user_c"
    assert distance, 13.45


@pytest.mark.parametrize("movie", ["a", "b", "c", "d", "e"])
def test_get_all_movieis_available(analysis, movie):
    assert movie in analysis.all_movieis_available()


def test_total_movieis_available(analysis):
    assert len(analysis.all_movieis_available()) == 5


def test_movies_not_seen(analysis):
    assert "c" and "e" in analysis.movies_not_seen("user_c")


@pytest.mark.parametrize("user", [dict(name="user_a",
                                       similarity=0.07,
                                       vote=3,
                                       movie="c"),
                                  dict(name="user_b",
                                       similarity=0.04,
                                       vote=3,
                                       movie="e")])
def test_who_saw_movie_not_seen(analysis, user):
    users_saw_movie = analysis.who_saw_movie_not_seen("user_c")
    assert len(users_saw_movie) == 2
    assert user['name'] in users_saw_movie
    assert user['similarity'] == users_saw_movie[user['name']]["similarity"]
    assert user["movie"] in users_saw_movie[user['name']]['movies']
    assert user["vote"] == users_saw_movie[user['name']]['movies'][user["movie"]]


def test_who_saw_movie_not_seen_not_contains_user(analysis):
    assert "user_d" not in analysis.who_saw_movie_not_seen("user_c")


def test_total_similarity_with_who_saw_movie_not_seen(analysis):
    similarity = analysis.total_similarity_with_who_saw_movie_not_seen('user_c')
    assert similarity['e']['sum_similarity'] == 0.04
    assert similarity['e']['sum_review'] == 0.12
    assert similarity['c']['sum_similarity'] == 0.07
    assert float("{:.2f}".format(similarity['c']['sum_review'])) == 0.21


@pytest.mark.parametrize("movie", [('c', 3),
                                   ('e', 3)])
def test_predict_movie_review(analysis, movie):
    assert movie in analysis.predict_movie_review('user_c')


def test_from_movielens():
    movielens = from_movielens()
    assert movielens.base == get_reviews()
