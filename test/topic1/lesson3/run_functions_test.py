import unittest

from src.topic1.lesson3.functions import function_task1, function_task2


class StTestCase(unittest.TestCase):

    def test_function_task1(self):
        self.assertTrue(type(function_task1()) == list)

    def test_function_task2(self):
        l1, l2 = [1, 2, 3], [1, 2, 3]
        self.assertTrue(function_task2(l1, l2) == l1 + l2)


if __name__ == '__main__':
    unittest.main()
