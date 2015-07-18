import unittest2 as unittest
from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.results = fibonacci(15)
    def tearDown(self):
        del self.results

    def test_1(self):
        numbers = [1, 2, 3, 5, 8, 13]
        j = 0
        for i in self.results:
            self.assertEqual(i, numbers[j])
            j += 1


if __name__ == "__main__":
    unittest.main()
