from Code.recomendacao import Recomendacao
import pytest
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def recomendacao():
    return Recomendacao(BASE_DIR+"/base.txt")


@pytest.mark.parametrize("user", [('user_a', 0.07),
                                  ('user_b', 0.04)])
def test_get_similares(recomendacao, user):
    assert user in recomendacao.get_similares('user_c').items()


@pytest.mark.parametrize("user", ["user_a", "user_b", "user_c"])
def test_list_all_users(recomendacao, user):
    assert user in recomendacao.all_users()


def test_more_similar(recomendacao):
    user_similar, distance = recomendacao.more_similar('user_a')
    print(user_similar, distance)
    assert user_similar == "user_c"
    assert distance, 13.45


@pytest.mark.parametrize("movie", ["a", "b", "c", "d", "e"])
def test_get_all_movieis_available(recomendacao, movie):
    assert movie in recomendacao.get_all_movieis_available()


def test_total_movieis_available(recomendacao):
    assert len(recomendacao.get_all_movieis_available()) == 5


def test_movies_not_seen(recomendacao):
    assert "c" and "e" in recomendacao.movies_not_seen("user_c")


@pytest.mark.parametrize("user", [dict(name="user_a",
                                       similarity=0.07,
                                       vote=3,
                                       movie="c"),
                                  dict(name="user_b",
                                       similarity=0.04,
                                       vote=3,
                                       movie="e")])
def test_who_saw_movie_not_seen(recomendacao, user):
    users_saw_movie = recomendacao.who_saw_movie_not_seen("user_c")
    assert len(users_saw_movie) == 2
    assert user['name'] in users_saw_movie
    assert user['similarity'] == users_saw_movie[user['name']]["similarity"]
    assert user["movie"] in users_saw_movie[user['name']]['movies']
    assert user["vote"] == users_saw_movie[user['name']]['movies'][user["movie"]]


def test_who_saw_movie_not_seen_not_contains_user(recomendacao):
    assert "user_d" not in recomendacao.who_saw_movie_not_seen("user_c")


def test_total_similarity_with_who_saw_movie_not_seen(recomendacao):
    similarity = recomendacao.total_similarity_with_who_saw_movie_not_seen('user_c')
    assert similarity['e']['sum_similarity'] == 0.04
    assert similarity['e']['sum_review'] == 0.12
    assert similarity['c']['sum_similarity'] == 0.07
    assert float("{:.2f}".format(similarity['c']['sum_review'])) == 0.21


@pytest.mark.parametrize("movie", [('c', 3),
                                   ('e', 3)])
def test_predict_movie_review(recomendacao, movie):
    assert movie in recomendacao.predict_movie_review('user_c')
