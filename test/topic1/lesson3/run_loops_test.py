import unittest
from src.topic1.lesson3.loops import loops_task1, loops_task2


class MyTestCase(unittest.TestCase):

    def test_loops_task1(self):
        self.assertTrue(loops_task1().__len__(), 500)

    def test_loops_task2(self):
        self.assertTrue(loops_task2(), [2, 4, 6, 8, 10])


if __name__ == '__main__':
    unittest.main()
