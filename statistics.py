from math import sqrt


def euclidean_distance(list_x, list_y):
    square = sqrt(sum([pow(list_x[item] - list_y[item], 2) for item in list_x if item in list_y]))
    return float("{:.2f}".format(square))


def degree_of_similarity(list_x, list_y):
    return float("{:.2f}".format(1/(1 + euclidean_distance(list_x, list_y))))
