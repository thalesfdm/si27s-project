import logging
import random

from src.csv import *
from src.nlp import *


def main():
    headers = get_headers("./data/dataset.csv")
    dataset = read_csv("./data/dataset.csv")

    logging.basicConfig(filename="log.txt", level=logging.DEBUG)

    dataset_prep = []
    project_list = []
    result = []

    for row in dataset:
        index = int(row[0])
        project = row[1].lower()
        description = preprocess(row[2])
        weight = int(row[3])

        dataset_prep.append([index, project, description, weight])
        project_list.append(project)

    project_list = list(set(project_list))
    project_list.sort(key=lambda f: int(f.split(" ")[1]))

    while len(project_list) > 3:
        p1 = random.choice(project_list)
        project_list.remove(p1)

        p2 = random.choice(project_list)
        project_list.remove(p2)

        test_data = [row for row in dataset_prep if row[1] in {p1, p2}]

        for item in test_data:
            best_value = 0
            best_index = 0
            for row in dataset_prep:
                if item[1] == row[1]:
                    continue
                similarity = item[2].similarity(row[2])
                if similarity > best_value:
                    best_value = similarity
                    best_index = row[0]
            item_index = item[0]
            logging.debug(
                f"\n{dataset[item_index - 1][2]}\n{dataset[best_index - 1][2]}\n"
            )
            result.append(dataset[item_index - 1][:-1] + dataset[best_index - 1][-1:])

    result.sort(key=lambda f: int(f[0]))
    write_csv("./data/result.csv", headers, result)


main()
