from src.nlp import *


def main():
    classified_backlog = [
        ['Criar novos usuários', 4, 4],
        ['Recuperar a senha de um usuário', 3, 4],
        ['Gerar relatórios de tráfego de usuários', 2, 5],
    ]

    classified_backlog_prep = []

    for item in classified_backlog:
        description = nlp(item[0])
        description = filter_sentence(description)
        description = lemmatisation(description)
        classified_backlog_prep.append([description, item[1], item[2]])

    non_classified_backlog = [
        ['Criação de um novo usuário'],
        ['Geração de relatórios de tráfego'],
    ]

    for nc_index, nc_item in enumerate(non_classified_backlog):
        nc_description = nlp(nc_item[0])
        best = 0
        index = 0
        for c_index, c_item in enumerate(classified_backlog_prep):
            c_description = nlp(c_item[0])
            similarity = c_description.similarity(nc_description)
            if similarity > best:
                best = similarity
                index = c_index
        # if best < 0.9: do something <--------- TO DO
        non_classified_backlog[nc_index].append(classified_backlog_prep[index][1])
        non_classified_backlog[nc_index].append(classified_backlog_prep[index][2])

    print(non_classified_backlog)


main()
