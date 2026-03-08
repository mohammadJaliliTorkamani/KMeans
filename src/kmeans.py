import random

from distance import euclidean_distance
from utils import compute_centroid, compute_ssd


class KMeans:

    def __init__(self, k, epsilon, max_iterations):
        self.k = k
        self.epsilon = epsilon
        self.max_iterations = max_iterations

        self.centroids = []
        self.clusters = []

    def initialize_centroids(self, dataset):
        self.centroids = random.sample(dataset, self.k)

    def assign_clusters(self, dataset):
        clusters = [[] for _ in range(self.k)]

        for point in dataset:

            distances = []
            for centroid in self.centroids:
                distances.append(euclidean_distance(point, centroid))

            min_index = distances.index(min(distances))
            clusters[min_index].append(point)

        return clusters

    def update_centroids(self, clusters):
        new_centroids = []

        for cluster in clusters:
            centroid = compute_centroid(cluster)

            if centroid is None:
                centroid = random.choice(self.centroids)

            new_centroids.append(centroid)

        return new_centroids

    def fit(self, dataset):
        self.initialize_centroids(dataset)

        previous_ssd = float('inf')

        current_ssd = None

        for iteration in range(self.max_iterations):  # As the first stop criterion

            self.clusters = self.assign_clusters(dataset)

            self.centroids = self.update_centroids(self.clusters)

            current_ssd = compute_ssd(self.clusters, self.centroids)

            if abs(previous_ssd - current_ssd) < self.epsilon:  # As the second stop criterion
                print(f"Second criterion stop met! converged at iteration {iteration}")
                break

            previous_ssd = current_ssd

        return self.clusters, self.centroids, current_ssd
