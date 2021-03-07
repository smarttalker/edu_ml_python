import unittest
from src.topic1.lesson3.classes_objects import class_task1


class StTestCase(unittest.TestCase):

    def test_loops_task1(self):
        car = class_task1()
        self.assertTrue(car.color, "white")
        self.assertTrue(car.name, "Tesla")


if __name__ == '__main__':
    unittest.main()
