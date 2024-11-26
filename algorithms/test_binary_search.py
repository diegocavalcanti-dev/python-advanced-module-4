import sys
import os

# Adiciona o diretório raiz ao Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest

from algorithms.binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        array = [3, 4, 5, 6, 7, 8, 9]
        find = 8

        result = binary_search(array, find, 0, len(array)-1)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()