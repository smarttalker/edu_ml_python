import unittest
from src.topic1.lesson3.loops import loops_task1


class StTestCase(unittest.TestCase):

    def test_loops_task1(self):
        self.assertTrue(loops_task1().__len__(), 500)


if __name__ == '__main__':
    unittest.main()
