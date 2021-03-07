import unittest
from src.topic1.lesson2.string_operations import string_operations_task1, string_operations_task2, string_operations_task3


class StTestCase(unittest.TestCase):

    def test_string_operations_task1(self):
        self.assertTrue(string_operations_task1().__len__(), 18)

    def test_string_operations_task2(self):
        self.assertTrue(string_operations_task2().isupper())

    def test_string_operations_task3(self):
        self.assertEqual(string_operations_task3(), 'tsesiw')


if __name__ == '__main__':
    unittest.main()
