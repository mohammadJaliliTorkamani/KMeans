import math


def compute_centroid(points):
    if not points:
        return None

    dimension = len(points[0])
    centroid = [0.0] * dimension

    for p in points:
        for i in range(dimension):
            centroid[i] += p[i]

    for i in range(dimension):
        centroid[i] /= len(points)

    return centroid


def compute_ssd(clusters, centroids):
    ssd = 0.0

    for i, cluster in enumerate(clusters):
        centroid = centroids[i]

        for point in cluster:
            dist = 0
            for j in range(len(point)):
                dist += math.pow(point[j] - centroid[j], 2)
            ssd += dist

    return ssd
