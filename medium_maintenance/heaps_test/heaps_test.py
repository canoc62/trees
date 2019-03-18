import unittest
from ..heaps.heaps import Heap

class HeapTestCase(unittest.TestCase):
    def setUp(self):
        self.array0 = []
        self.array1 = [1]
        self.array2 = [3, 7, 1, 11, 2, 4, 5, 10]
        self.array3 = [2, -1, 4, 10, 1, 7, 22]
        self.heap0 = Heap(self.array0)
        self.heap1 = Heap(self.array1)
        self.heap2 = Heap(self.array2)
        self.heap3 = Heap(self.array3)

    def test_heapsort(self):
        self.assertEqual(self.heap0.data, [], "Invalid heap.")
        self.assertEqual(self.heap1.data, [1], "Invalid heap.")
        self.assertEqual(self.heap2.data, [11, 10, 5, 7, 2, 4, 1, 3], "Invalid heap.")
        self.assertEqual(self.heap3.data, [22, 10, 7, -1, 1, 2, 4], "Invalid heap.")

    def test_insert(self):
        self.heap0.insert(1)
        self.heap1.insert(4)
        self.heap2.insert(8)
        self.heap3.insert(3)

        self.assertEqual(self.heap0.data, [1], "Invalid heap.")
        self.assertEqual(self.heap1.data, [4, 1], "Invalid heap.")
        self.assertEqual(self.heap2.data, [11, 10, 5, 8, 2, 4, 1, 3, 7], "Invalid heap.")
        self.assertEqual(self.heap3.data, [22, 10, 7, 3, 1, 2, 4, -1], "Invalid heap.")

    def test_delete(self):
        deleted0 = self.heap0.delete(0)
        deleted1 = self.heap1.delete(0)
        deleted2 = self.heap2.delete(4)
        deleted3 = self.heap3.delete(6)

        self.assertEqual(deleted0, None, "Incorrect delete value returned.")
        self.assertEqual(deleted1, None, "Incorrect delete value returned.")
        self.assertEqual(deleted2, None, "Incorrect delete value returned.")
        self.assertEqual(deleted3, None, "Incorrect delete value returned.")

        self.assertEqual(self.heap0.data, [], "Invalid heap after deletion.")
        self.assertEqual(self.heap1.data, [], "Invalid heap after deletion.")
        self.assertEqual(self.heap2.data, [11, 10, 5, 7, 3, 4, 1], "Invalid heap after deletion.")
        self.assertEqual(self.heap3.data, [22, 10, 7, -1, 1, 2], "Invalid heap after deletion.")


    def test_extract(self):
        extracted0 = self.heap0.extract()
        extracted1 = self.heap1.extract()
        extracted2 = self.heap2.extract()
        extracted3 = self.heap3.extract()

        self.assertEqual(extracted0, None, "Incorrect extracted value returned.")
        self.assertEqual(extracted1, None, "Incorrect extracted value returned.")
        self.assertEqual(extracted2, None, "Incorrect extracted value returned.")
        self.assertEqual(extracted3, None, "Incorrect extracted value returned.")

        self.assertEqual(self.heap0.data, [], "Invalid heap after extraction.")
        self.assertEqual(self.heap1.data, [], "Invalid heap after extraction.")
        self.assertEqual(self.heap2.data, [10, 7, 5, 3, 2, 4, 1], "Invalid heap after extraction.")
        self.assertEqual(self.heap3.data, [10, 4, 7, -1, 1, 2], "Invalid heap after extraction.")
