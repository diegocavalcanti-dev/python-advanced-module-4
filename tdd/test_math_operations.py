import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest

from tdd.math_operations import addition_operation, subtraction_operation


class TestMathOperations(unittest.TestCase):
    def test_addition_operation(self):
        math_addition_result = addition_operation(num_1=5, num_2=10)
        self.assertEqual(math_addition_result, 15)
        
    def test_subtraction_operation(self):
        math_subtraction_result = subtraction_operation(num_1=10, num_2=10)
        self.assertEqual(math_subtraction_result, 0)


if __name__ == '__main__':
    unittest.main()
    
# python -m unittest tdd.test_math_operations    --- COMANDO NECESSÁRIO