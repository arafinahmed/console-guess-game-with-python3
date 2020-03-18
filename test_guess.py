import unittest
from guess import *

class TestGuess(unittest.TestCase):
    def test_setAnswer(self):
        res = setAnswer(1, 10)
        self.assertTrue(res)
    def test_startGame(self):
        res = startGame(1, 1,5)
        self.assertTrue(res)


if __name__ == "__main__":
    unittest.main()
        

