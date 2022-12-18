import unittest
import sys
import math
sys.path.append("./practice1")
import command as cmd

class Testcommand(unittest.TestCase):
    def setUp(self) -> None:
        self.cmd = cmd

    def test_calcul(self):
        ls = [[0.0, 0.0], [1.0, 1.0]]
        res = self.cmd.calcul(ls)
        print(res)
        self.assertEqual(res, [[math.pi/4, 2**0.5]])

if __name__ == "__main__":
    unittest.main()