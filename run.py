from src.csv import *
from src.nlp import *


def main():
    headers = get_headers('./data/classified_backlog.csv')
    classified_backlog = read_csv('./data/classified_backlog.csv')
    non_classified_backlog = read_csv('./data/non_classified_backlog.csv')

    classified_backlog_prep = []
    non_classified_backlog_prep = []

    for item in classified_backlog:
        description = nlp(item[0])
        description = filter_sentence(description)
        description = lemmatisation(description)
        classified_backlog_prep.append([description, item[1], item[2]])

    for item in non_classified_backlog:
        description = nlp(item[0])
        description = filter_sentence(description)
        description = lemmatisation(description)
        non_classified_backlog_prep.append([description, item[1], item[2]])

    for nc_index, nc_item in enumerate(non_classified_backlog_prep):
        nc_description = nlp(nc_item[0])
        best = 0
        index = 0
        for c_index, c_item in enumerate(classified_backlog_prep):
            c_description = nlp(c_item[0])
            similarity = c_description.similarity(nc_description)
            if similarity > best:
                best = similarity
                index = c_index
        if best >= 0.75:
            non_classified_backlog_prep[nc_index][1] = classified_backlog_prep[index][1]
            non_classified_backlog_prep[nc_index][2] = classified_backlog_prep[index][2]

    write_csv('./data/newly_classified_backlog.csv', headers, non_classified_backlog_prep)


main()
