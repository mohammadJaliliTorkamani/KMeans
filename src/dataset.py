import csv


def load_csv(filepath, selected_columns):
    dataset = []

    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            point = []

            for col in selected_columns:
                point.append(float(row[col]))

            dataset.append(point)

    return dataset
