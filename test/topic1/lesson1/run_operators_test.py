import unittest

from src.topic1.lesson1.operators import operators_task1, operators_task2, operators_task3


class StTestCase(unittest.TestCase):

    def test_operators_task1(self):
        self.assertTrue(operators_task1() == 10)

    def test_operators_task2(self):
        self.assertTrue(operators_task2())

    def test_operators_task3(self):
        self.assertTrue(operators_task3())


if __name__ == '__main__':
    unittest.main()
