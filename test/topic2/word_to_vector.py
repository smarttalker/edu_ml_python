import unittest
from src.topic2.word_to_vector import collect_all_unique_words, to_lowercase_and_remove_stop_words, matrixObject


class MyTestCase(unittest.TestCase):

    def test_collect_all_unique_words(self):
        self.assertEqual(collect_all_unique_words(['apple', 'b', 'c', 'apple', 'apple', 'c']), ['apple', 'b', 'c'])

    def test_to_lowercase_and_remove_stop_words(self):
        stop_words_list = ['to', 'and']
        list_of_words = ['Hello', 'ABC', 'to', 'and']
        res = to_lowercase_and_remove_stop_words(list_of_words, stop_words_list)
        self.assertEqual(res, ['hello', 'abc'])

    def test_matrix(self):
        matrix = matrixObject(count_of_columns=10)
        matrix.extend_matrix("TEST hello hello hello".split())
        self.assertEqual(matrix.get_title(), ['hello', 'test'])



if __name__ == '__main__':
    unittest.main()
