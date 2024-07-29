# urllib
import urllib.request
url = "https://google.com"

response = urllib.request.urlopen(url)
# print(response.read())

#unittest
import unittest
def add(x, y):
    return x + y

class TestAdd(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2) ,3)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1 ,-2) ,-3)

    def test_add_negaposi_numbers(self):
        self.assertEqual(add(-1, 2), 1)

unittest.main()