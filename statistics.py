from __future__ import division
from math import sqrt


def euclidean_distance(list_x, list_y):
    variance = [pow(list_x[item] - list_y[item], 2) for item in list_x if item in list_y]
    if variance:
        return float("{:.2f}".format(sqrt(sum(variance))))
    return -1


def degree_of_similarity(list_x, list_y):
    try:
        return float("{:.2f}".format(1/(1 + euclidean_distance(list_x, list_y))))
    except ZeroDivisionError:
        return 0.
