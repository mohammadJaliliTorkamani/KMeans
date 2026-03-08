import math


def euclidean_distance(p1, p2):
    total = 0.0

    for i in range(len(p1)):
        total += math.pow(p1[i] - p2[i], 2)

    return math.sqrt(total)
