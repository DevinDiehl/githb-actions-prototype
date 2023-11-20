import unittest
from main import returnBackwardsString


class TestMain(unittest.TestCase):
    def testReturnBackwardsString(self):
        string = "this is my test string"
        reversedString = "gnirts tset ym si siht"
        self.assertEqual(reversedString, returnBackwardsString(string))


if __name__ == "__main__":
    unittest.main()
