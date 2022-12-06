import unittest
from ecc_input import *


class TestCSVFile(unittest.TestCase):

    def TestGetData(self):
        test.assertEqual(get_data(3, 15),)
        test.assertEqual(get_data(1, 1))

class TestNumericalCSVFile(unittest.TestCase):

    def TestGetData(self):
        test.assertEqual(get_data(3, 15), "[['01-01-2012', 266.0]]")