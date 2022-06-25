import unittest

import atm1
from atm1 import Balance,pin_number
from atm1 import pin_number
class TestAtm(unittest.TestCase):
    def test_Balance(self):
  #make sure value errors are raised when necessry

     self.assertRaises(ValueError, Balance, -50, -2)
     self.assertRaises(SystemExit, Balance, 500, 600)
     ##with self.assertRaises(ValueError):
        ##atm1.Balance(-10, -2)





if __name__ == '__main__':
    unittest.atm1()