import string
import nltk


"""
Why word vectors?

Word Embedding is a language modeling technique used for mapping words to vectors of real numbers.
It represents words or phrases in vector space with several dimensions.

Poetry is, at its core, the art of identifying and manipulating linguistic similarity.
similarity and simple linear algebra

@see https://www.baeldung.com/cs/convert-word-to-vector
"""
# Do not change the sentences
sentence1 = "Socrates likes to watch movies. Mary likes movies too."
sentence2 = "Rene Descartes likes to watch movies. Mary likes movies too."
sentence3 = "Kant also likes to watch football games"

def collect_all_unique_words(list_of_words):
    """
    1. all unique words have to be collected to the list
    """
    # example 1
    # unique_words = list(set(list_of_sentences))

    # example 2
    unique_words = list()
    for w in list_of_words:
        if unique_words.count(w) == 0:
            unique_words.append(w)

    unique_words.sort(reverse=False)
    # example 3 please use HOF 'map, filter, zip'
    return unique_words

def st_collect_all_unique_words(list_of_sentences):
    """
    1. all unique words have to be collected to the list
    """
    # TODO 1 use HOF 'map, filter, etc'
    collect_words = []
    list_of_sentences = st_to_lowercase_and_remove_stop_words(list_of_sentences)
    for sentence in  list_of_sentences:
        for tmp_word in sentence:
            if not tmp_word in collect_words:
                collect_words.append(tmp_word)
    return collect_words

def to_lowercase_and_remove_stop_words(list_of_words, stop_words_list):
    """
    1. Uppercase should be transform to lower case. For example 'Hello' -> 'hello'
    2. Remove all STOP WORDS like - 'too, and, etc'

    """
    res = list(filter(lambda x: stop_words_list.count(x) == 0, list_of_words))
    res = list(map(lambda x: x.lower(), res))
    return res


def st_to_lowercase_and_remove_stop_words(list_of_sentences):
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

def st_create_matrix(list_of_sentences, list_unique_words): #изменил параметр
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






class matrixObject():

    def __init__(self, count_of_columns, stop_words_list=None, matrix_title_list=None):
        if stop_words_list is None: stop_words_list = []
        if matrix_title_list is None: matrix_title_list = []
        self.count_of_columns = count_of_columns
        self.stop_words_list = stop_words_list
        self.matrix_title_list = matrix_title_list
        self.vector_matrix = []

    def update_title(self, list_of_words):
        res = collect_all_unique_words(list_of_words)
        res = to_lowercase_and_remove_stop_words(res, self.stop_words_list)
        return res

    def extend_matrix(self, list_of_words):
        res = self.update_title(list_of_words)
        self.matrix_title_list = collect_all_unique_words(res + self.matrix_title_list)
        self.vector_matrix.append(list(map(lambda w: res.count(w), self.matrix_title_list)))

    def print_matrix(self):
        print(self.matrix_title_list)
        list(map(lambda w: print(w), self.vector_matrix))

    def get_title(self):
        return self.matrix_title_list







if __name__ == '__main__':
    '''
    we need to deal with linguistic entities such as words?
    How can we model them as mathematical representations? The answer is we convert them to vectors!
    '''
    list_unique_words = st_collect_all_unique_words([sentence1, sentence2, sentence3])
    print("Список уникальных слов:\n", ", ".join(list_unique_words))
    st_create_matrix([sentence1, sentence2, sentence3], list_unique_words)

    # TODO 3 create the matrix where count of COLUMNS is unique words and ROWS count of sentences

    # https://www.baeldung.com/cs/convert-word-to-vector#one-hot-vectors
    # vector where each column corresponds to a word



    list_for_matrix = ["Socrates Socrates likes to watch movies. Mary likes movies too.",
                       "Rene Descartes likes to watch movies. Mary likes movies too.",
                       "Kant, also likes to watch football games",
                       "Test",
                       "Hello"]

    '''
    We need to deal with linguistic entities such as words?
    How can we model them as mathematical representations? The answer is we convert them to vectors!
    '''
    matrix = matrixObject(count_of_columns=10)
    for i in list_for_matrix:
        matrix.extend_matrix(i.split())

    matrix.print_matrix()