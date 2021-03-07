import unittest

from src.topic1.exam1 import loops_exam1


class StTestCase(unittest.TestCase):

    def test_loops_task2(self):
        self.assertEqual(loops_exam1(), [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])


if __name__ == '__main__':
    unittest.main()
