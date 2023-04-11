from Excercise1 import mat_to_list
import unittest

class TestMatrixList(unittest.TestCase):

    def test_mat_to_list(self):
        adj_mat = [[0, 1, 0, 1, 0, 0],
                   [0, 0, 1, 0, 0, 0],
                   [1, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0]]

        res = [[1, 3], [2], [0], [4], [3], []]
        adj_list = mat_to_list(adj_mat)
        self.assertListEqual(adj_list, res, msg="Adjacency List is not correct")

    def test_true(self):
        adj_mat = [[0, 1, 0, 1, 0, 0],
                   [0, 0, 1, 0, 0, 0],
                   [1, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0]]

        res = mat_to_list(adj_mat)

        self.assertTrue(res == [[1, 3], [2], [0], [4], [3], []] or res == [[1, 3], [2], [0], [4], [3], [0, 1, 2]], f"Error: {res} is not a valid output")



if __name__== '__main__':
    unittest.main()