# K-Means Clustering Project – Assignment 4

**Course:** CSCE-474/874 – Introduction to Data Mining  
**University:** University of Nebraska–Lincoln (UNL)  
**Group Members:** Mohammad Jalili Torkamani, Amirmohammad Sadeghnejad, Pedro Gomes, Jason Le  
**Assignment:** HW-4  

---

## Project Overview

This project implements the K-Means clustering algorithm in Python from scratch.

Features:
- Reads datasets from CSV files with continuous attributes.
- Uses configurable number of clusters (k), epsilon, and max iterations.
- Outputs cluster details, centroids, SSD, and runtime.
- Generates performance plots:
  - Runtime vs k
  - Runtime vs dataset size
  - Runtime vs dimensions
  - Exploring different k
- Fully Dockerized for reproducibility.

Note: For this assignment, we used the TMDb Movies Dataset (2023), available on Kaggle at https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies, which we downloaded on March 8, 2026 and is used in our final project. To ensure manageable computation and runtime during experiments, we limited our analysis to the first 10,000 records of the dataset. All clustering operations were performed on this subset.

---

## Project Structure

KMeans/

├── Dockerfile

├── docker-compose.yml

├── requirements.txt

├── src/

│   ├── main.py

│   ├── kmeans.py

│   ├── dataset.py

│   ├── distance.py

│   ├── utils.py

│   ├── experiments.py

│   └── results_writer.py

├── data/

│   └── dataset.csv

└── output/

---

## How to Run

### 1. Build the Docker image

    docker compose build

### 2. Run the project

    docker compose up

Results will be saved inside the `output/` folder.

---

## Output Files

- kmeans_results.txt
- runtime_vs_k.png
- runtime_vs_dataset_size.png
- runtime_vs_dimensions.png
- different_k_method.png

---

## Configuration

### Change Columns
Edit `COLUMNS` in Dockerfile:

environment:
  - COLUMNS=x1,x2,x3

### Change Algorithm Parameters
Edit the command in docker-compose.yml: 

python main.py <k> <epsilon> <max_iterations> /app/data/dataset.csv

Example command: 

"python main.py 3 0.001 100 /app/data/dataset.csv"