import unittest
from calculator import Calculator


def setUpModule():
  print('set up module')

def tearDownModule():
  print('tear down module')

class TestCalculator(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    print('Set up class')
    # Create an instance of the calculator that can be used in all tests
    self.calc = Calculator()

  @classmethod
  def tearDownClass(self):
    print('Tear down class')

  def test_add(self):
    self.assertEqual(self.calc.add(2, 7), 9)

  def test_subtract(self):
    self.assertEqual(self.calc.subtract(7, 2), 5)

  def test_divide(self):
    self.assertEqual(self.calc.divide(25, 5), 5)

  def test_multiply(self):
    self.assertEqual(self.calc.multiply(5, 5), 25)

  # Write test methods for subtract, multiply, and divide

if __name__ == '__main__':
    unittest.main()
