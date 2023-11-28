import unittest

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def power(x, y):
    """Calculate x raised to the power y without using math.pow."""
    result = 1
    for _ in range(int(y)):
        result *= x
    return result

class TestMyFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 4), 9) 

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12) 

    def test_power(self):
        self.assertEqual(power(2, 8), 256)  

    def test_power_with_zero(self):
        self.assertEqual(power(2, 0), 1)  



if __name__ == '__main__':
    unittest.main()
