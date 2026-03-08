import time

import matplotlib.pyplot as plt

from kmeans import KMeans


def runtime_vs_k(dataset, epsilon, max_iter, k_values):
    runtimes = []

    for k in k_values:
        model = KMeans(k, epsilon, max_iter)

        start = time.time()
        model.fit(dataset)
        end = time.time()

        runtimes.append(end - start)

    plt.figure()
    plt.plot(k_values, runtimes, marker='o')
    plt.xlabel("Number of Clusters (k)")
    plt.ylabel("Runtime (seconds)")
    plt.title("Runtime vs Number of Clusters")
    plt.grid(True)

    plt.savefig("/app/output/runtime_vs_k.png")
    plt.close()


def runtime_vs_dataset_size(dataset, epsilon, max_iter, k):
    sizes = []
    runtimes = []

    step = max(1, int(len(dataset) / 10))

    for size in range(step, len(dataset) + 1, step):
        subset = dataset[:size]

        model = KMeans(k, epsilon, max_iter)

        start = time.time()
        model.fit(subset)
        end = time.time()

        sizes.append(size)
        runtimes.append(end - start)

    plt.figure()
    plt.plot(sizes, runtimes, marker='o')
    plt.xlabel("Dataset Size (Transactions)")
    plt.ylabel("Runtime (seconds)")
    plt.title("Runtime vs Dataset Size")
    plt.grid(True)

    plt.savefig("/app/output/runtime_vs_dataset_size.png")
    plt.close()


def runtime_vs_dimensions(dataset, epsilon, max_iter, k):
    dims = len(dataset[0])

    dim_values = []
    runtimes = []

    for d in range(1, dims + 1):
        reduced = [point[:d] for point in dataset]

        model = KMeans(k, epsilon, max_iter)

        start = time.time()
        model.fit(reduced)
        end = time.time()

        dim_values.append(d)
        runtimes.append(end - start)

    plt.figure()
    plt.plot(dim_values, runtimes, marker='o')
    plt.xlabel("Number of Dimensions")
    plt.ylabel("Runtime (seconds)")
    plt.title("Runtime vs Dimensions")
    plt.grid(True)

    plt.savefig("/app/output/runtime_vs_dimensions.png")
    plt.close()


def different_k_method(dataset, epsilon, max_iter, max_k=10):
    k_values = list(range(1, max_k + 1))
    ssds = []

    for k in k_values:
        model = KMeans(k, epsilon, max_iter)
        _, _, ssd = model.fit(dataset)

        ssds.append(ssd)

    plt.figure()
    plt.plot(k_values, ssds, marker='o')
    plt.xlabel("Number of Clusters (k)")
    plt.ylabel("SSD")
    plt.title("Optimal k Explorer")
    plt.grid(True)

    plt.savefig("/app/output/different_k_method.png")
    plt.close()
