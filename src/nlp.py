import spacy

nlp = spacy.load("pt_core_news_md")


def filter_sentence(text):
    filtered_sentence = [token.text for token in text if not token.is_stop]
    return nlp(" ".join(filtered_sentence))


def lemmatisation(text):
    lemmatised = [token.lemma_ for token in text]
    return nlp(" ".join(lemmatised))
