import statistics


def test_euclidean_distance():
    vector_a = dict(a=1, b=2, c=3, d=4)
    vector_b = dict(a=1, b=2, c=5, d=4)
    assert statistics.euclidean_distance(vector_a, vector_b) == 2


def test_degree_of_similarity():
    vector_a = dict(a=1, b=2, c=3, d=4)
    vector_b = dict(a=1, b=2, c=5, d=4)
    assert statistics.degree_of_similarity(vector_a, vector_b) == 0.33