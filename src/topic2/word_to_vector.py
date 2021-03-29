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
    return None


def to_lowercase_and_remove_stop_words(list_of_sentences):
    """
    1. Uppercase should be transform to lower case. For example 'Hello' -> 'hello'
    2. Remove all STOP WORDS like - 'to, and, etc' Create you own list

    """
    # TODO 2
    return None


def create_matrix(list_of_sentences, count_of_columns):
    """
    type of the matrix will be 'int'
    Title of the matrix == our unique words

    TITLE---------------------'movies'--'watch'--'football'--'...'
    3 line of the matrix 'int''   1  '--'  1  '--'   0   '--'...'
                              '   1  '--'  1  '--'   0   '--'...'
                              '   0  '--'  1  '--'   1   '--'...'
    """
    # TODO 3 collect all unique words from the all sentences
    return None


if __name__ == '__main__':
    '''
    we need to deal with linguistic entities such as words?
    How can we model them as mathematical representations? The answer is we convert them to vectors!
    '''

    # TODO 3 create the matrix where count of COLUMNS is unique words and ROWS count of sentences

    # https://www.baeldung.com/cs/convert-word-to-vector#one-hot-vectors
    # vector where each column corresponds to a word
