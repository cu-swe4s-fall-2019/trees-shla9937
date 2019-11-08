import unittest
import random
import binary_tree
from binary_tree import Tree
from binary_tree import Node


class TestBinaryTree(unittest.TestCase):

    def test_insert_value(self):
        bst = Tree()
        r = bst.insert([10, 2])
        self.assertEqual(r, True)

    def test_insert_values(self):
        bst = Tree()
        for i in [[10, 1], [12, 2], [17, 3], [14, 4], [15, 5]]:
            r = bst.insert(i)
            self.assertEqual(r, True)

    def test_insert_same_key(self):
        bst = Tree()
        for i in [[10, 1], [12, 2], [17, 3], [14, 4], [15, 5]]:
            bst.insert(i)
        r = bst.insert([12, 4])
        self.assertEqual(r, False)

    def test_insert_rand_value(self):
        bst = Tree()
        k = [random.randint(1, 100),
             random.randint(1, 100)]
        r = bst.insert(k)
        self.assertEqual(r, True)

    def test_insert_rand_values(self):
        for num in range(100):
            bst = Tree()
            L = []
            M = []
            for i in range(100):
                rand_int = random.randint(1, 100)
                if rand_int not in L:
                    L.append(rand_int)
            for j in L:
                rand_ints = []
                rand_int_2 = random.randint(1, 100)
                rand_ints.append(j)
                rand_ints.append(rand_int_2)
                M.append(rand_ints)
            for k in M:
                r = bst.insert(k)
                self.assertEqual(r, True)

    def test_cannot_find_value(self):
        bst = Tree()
        for i in [[10, 1], [12, 2], [17, 3], [14, 4], [15, 5]]:
            bst.insert(i)
        r = bst.search(20)
        self.assertEqual(r, False)

    def test_find_value(self):
        bst = Tree()
        for i in [[10, 1], [12, 2], [17, 3], [14, 4], [15, 5]]:
            bst.insert(i)
        r = bst.search(12)
        self.assertEqual(r, [12, 2])

    def test_find_same_value(self):
        bst = Tree()
        for i in [[10, 1], [12, 2], [12, 3], [17, 3], [14, 4], [15, 5]]:
            bst.insert(i)
        r = bst.search(12)
        self.assertEqual(r, [12, 2, 3])

    def test_find_rand_value(self):
        bst = Tree()
        for i in [[10, 1], [12, 2], [11, 3], [14, 4], [13, 5]]:
            bst.insert(i)
        for j in range(100):
            search_for = random.randint(10, 14)
            r = bst.search(search_for)
            if search_for == 10:
                s = [10, 1]
            elif search_for == 11:
                s = [11, 3]
            elif search_for == 12:
                s = [12, 2]
            elif search_for == 13:
                s = [13, 5]
            elif search_for == 14:
                s = [14, 4]
            self.assertEqual(r, s)


if __name__ == '__main__':
    unittest.main()
