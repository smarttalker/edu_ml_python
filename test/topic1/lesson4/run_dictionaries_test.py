import unittest
from src.topic1.lesson4.dictionaries import dictionary_task1


class StTestCase(unittest.TestCase):

    def test_loops_task1(self):
        self.assertEqual(dictionary_task1()["Max"], +38097212199)


if __name__ == '__main__':
    unittest.main()
