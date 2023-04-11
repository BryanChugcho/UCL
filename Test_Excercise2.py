from Excercise2 import reachable
import unittest

class TestReachable(unittest.TestCase):
    def test_reachable(self):
        adj_list = [[1, 3], [2], [0], [4], [3], []]
        start_node = 0
        res = reachable(adj_list, start_node)
        self.assertTrue(res == {0, 1, 2, 3, 4} or res == {3, 4}, f"Error: {res} is not a valid output")




if __name__== '__main__':
    unittest.main()