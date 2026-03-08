import argparse
import os
import time

from dataset import load_csv
from experiments import (
    runtime_vs_k,
    runtime_vs_dataset_size,
    runtime_vs_dimensions,
    different_k_method
)
from kmeans import KMeans
from results_writer import write_results


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("k", type=int)
    parser.add_argument("epsilon", type=float)
    parser.add_argument("max_iterations", type=int)
    parser.add_argument("dataset", type=str)

    args = parser.parse_args()

    columns_env = os.getenv("COLUMNS")

    if columns_env:
        selected_columns = columns_env.split(",")
    else:
        selected_columns = ["revenue", "runtime", "vote_average", "vote_count"]

    print("Using columns:", selected_columns)

    dataset = load_csv(args.dataset, selected_columns)

    model = KMeans(args.k, args.epsilon, args.max_iterations)

    start_time = time.time()
    clusters, centroids, ssd = model.fit(dataset)
    end_time = time.time()

    runtime = end_time - start_time

    write_results("/app/output/kmeans_results.txt", clusters, centroids, ssd, runtime)

    runtime_vs_k(dataset, args.epsilon, args.max_iterations, range(1, 10))
    runtime_vs_dataset_size(dataset, args.epsilon, args.max_iterations, args.k)
    runtime_vs_dimensions(dataset, args.epsilon, args.max_iterations, args.k)
    different_k_method(dataset, args.epsilon, args.max_iterations, 10)


if __name__ == "__main__":
    main()
