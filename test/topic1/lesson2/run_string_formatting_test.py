import unittest

from src.topic1.lesson2.string_formatting import string_formatting_task1


class StTestCase(unittest.TestCase):

    def test_string_formatting_task1(self):
        string_formatting_task1()
        self.assertEqual(string_formatting_task1(), "Hello John Doe. Your current balance is $53.44")


if __name__ == '__main__':
    unittest.main()
