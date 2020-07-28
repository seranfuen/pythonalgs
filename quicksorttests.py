import unittest
from quicksort import QuickSort

class TestQuickSort(unittest.TestCase):
    def test_random_array(self):
        arr = [8, 1, -5, 3, 2, 2, -8, 10]
        result = QuickSort().sort(arr)
        self.assertEqual(result, [-8, -5, 1, 2, 2, 3, 8, 10])
        
    def test_sorted_array(self):
        arr = [-8, -5, 1, 2, 2, 3, 8, 10]
        result = QuickSort().sort(arr)
        self.assertEqual(result, [-8, -5, 1, 2, 2, 3, 8, 10])
        
    def test_array_all_same(self):
        arr = [1, 1, 1]
        result = QuickSort().sort(arr)
        self.assertEqual([1, 1, 1], result)
        
    def test_empty_Array(self):
        arr = []
        result = QuickSort().sort(arr)
        self.assertEqual([], result)
        
    def test_reverse_sorted_array(self):
        arr = [5, 3, 1, -4, -6]
        result = QuickSort().sort(arr)
        self.assertEqual([-6, -4, 1, 3, 5], result)
        
if __name__ == '__main__':
    unittest.main()