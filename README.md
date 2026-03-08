# K-Means Clustering Project - Homework Assignment 4

**Course:** CSCE-474/874 – Introduction to Data Mining  
**University:** University of Nebraska-Lincoln (UNL)  
**Group Members:** Mohammad Jalili Torkamani, Amirmohammad Sadeghnejad, Pedro Gomes, Jason Le  
**Assignment:** HW-4

---

## Project Overview

This project implements the **K-Means clustering algorithm** in Python. It is designed to:

- Read datasets from CSV files with continuous attributes.
- Cluster data based on a specified number of clusters (`k`), a convergence threshold (`epsilon`), and a maximum number of iterations.
- Output cluster centroids, cluster members, and the **sum of squared distances (SSD)**.
- Record **runtime and clustering performance plots** for analysis.
- Evaluate runtime as a function of **number of clusters**, **dataset size**, and **number of dimensions**.
- Determine the **optimal number of clusters** using the **Elbow method**.

The project is fully **Dockerized** to allow reproducible execution on any system without manual dependency installation.

---

## Directory Structure

```text
kmeans-project/
│
├── Dockerfile                   # Docker image definition
├── docker-compose.yml           # Compose file for easy execution
├── requirements.txt             # Python dependencies
│
├── src/                         # Python source code
│   ├── main.py                  # Main execution file
│   ├── kmeans.py                # K-Means algorithm implementation
│   ├── dataset.py               # CSV dataset loading utility
│   ├── distance.py              # Distance computation utilities
│   ├── utils.py                 # Helper functions
│   ├── experiments.py           # Runtime & Elbow method analysis
│   └── results_writer.py        # Output file writer
│
├── data/                        # Input CSV dataset(s)
│   └── dataset.csv
│
└── output/                      # Generated results and plots