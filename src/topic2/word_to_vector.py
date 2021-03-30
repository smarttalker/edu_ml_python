import string
import nltk


"""
Why word vectors?

Word Embedding is a language modeling technique used for mapping words to vectors of real numbers.
It represents words or phrases in vector space with several dimensions.

Poetry is, at its core, the art of identifying and manipulating linguistic similarity.
similarity and simple linear algebra

@see https://www.baeldung.com/cs/convert-word-to-vector

TFFDF
PMI
Word Embeddings (CBO)
"""

# Do not change the sentences
sentence1 = "Socrates likes to watch movies. Mary likes movies too."
sentence2 = "Rene Descartes likes to watch movies. Mary likes movies too."
sentence3 = "Kant also likes to watch football games"


def collect_all_unique_words(list_of_sentences):
    """
    1. all unique words have to be collected to the list
    """
    # TODO 1 use HOF 'map, filter, etc'
    collect_words = []
    list_of_sentences = to_lowercase_and_remove_stop_words(list_of_sentences)
    for sentence in  list_of_sentences:
        for tmp_word in sentence:
            if not tmp_word in collect_words:
                collect_words.append(tmp_word)
    return collect_words


def to_lowercase_and_remove_stop_words(list_of_sentences):
    """
    1. Uppercase should be transform to lower case. For example 'Hello' -> 'hello'
    2. Remove all STOP WORDS like - 'to, and, etc' Create you own list
    """
    # TODO 2
    stopwords = nltk.corpus.stopwords.words('english')      #список стопслов
    tt = str.maketrans(dict.fromkeys(string.punctuation))   #список знаков препинания
    result_list = []
    for sentence in list_of_sentences:
        result_list.append(list(filter(lambda x: not x in stopwords, sentence.lower().translate(tt).split())))
    return result_list


def create_matrix(list_of_sentences, list_unique_words): #изменил параметр
    """
    type of the matrix will be 'int'
    Title of the matrix == our unique words

    TITLE---------------------'movies'--'watch'--'football'--'...'
    3 line of the matrix 'int''   1  '--'  1  '--'   0   '--'...'
                              '   1  '--'  1  '--'   0   '--'...'
                              '   0  '--'  1  '--'   1   '--'...'
    """
    # TODO 3 collect all unique words from the all sentences
    print("\n")
    for u_word in list_unique_words:
        print(u_word, end="\t")
    print("\n")
    for sentence in range(len(list_of_sentences)):
        tmp_list = list_of_sentences[sentence].lower()
        for u_word in list_unique_words:
            if tmp_list.find(u_word) == -1:
                print(0, end="\t\t")
            else:
                print(1, end="\t\t")
        print("\n")

    return None


if __name__ == '__main__':
    '''
    we need to deal with linguistic entities such as words?
    How can we model them as mathematical representations? The answer is we convert them to vectors!
    '''
    list_unique_words = collect_all_unique_words([sentence1, sentence2, sentence3])
  #  print("Список уникальных слов:\n", ", ".join(list_unique_words))
    create_matrix([sentence1, sentence2, sentence3], list_unique_words)

    # TODO 3 create the matrix where count of COLUMNS is unique words and ROWS count of sentences

    # https://www.baeldung.com/cs/convert-word-to-vector#one-hot-vectors
    # vector where each column corresponds to a word
