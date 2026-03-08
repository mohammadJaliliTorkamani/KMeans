import datetime
import os

os.makedirs("output", exist_ok=True)


def write_results(filepath, clusters, centroids, ssd, runtime):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, "w") as f:

        f.write("K-Means Clustering Results\n")
        f.write(f"Timestamp: {datetime.datetime.now()}\n\n")

        f.write(f"Final SSD: {ssd}\n")
        f.write(f"Runtime: {runtime} seconds\n\n")

        for i, cluster in enumerate(clusters):

            f.write(f"Cluster {i + 1}\n")
            f.write(f"Centroid: {centroids[i]}\n")
            f.write(f"Number of points: {len(cluster)}\n")

            f.write("Points:\n")
            for p in cluster:
                f.write(f"{p}\n")

            f.write("\n")
