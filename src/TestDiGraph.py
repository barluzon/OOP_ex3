import unittest
from unittest import TestCase
from src.DiGraph import DiGraph


class TestDiGraph(TestCase):

    def setUp(self) -> None:
        self.graph = DiGraph()
        for i in range(4):
            self.graph.add_node(i)

        self.graph.add_edge(0, 1, 1)
        self.graph.add_edge(1, 0, 1)
        self.graph.add_edge(1, 2, 1)
        self.graph.add_edge(2, 3, 1)
        self.graph.add_edge(3, 1, 1)

    def test_v_size(self):
        size = self.graph.v_size()
        expected = 4
        self.assertEqual(size, expected)

    def test_e_size(self):
        size = self.graph.e_size()
        expected = 5
        self.assertEqual(size, expected)

    def test_get_all_v(self):
        all_v = list(self.graph.get_all_v())
        expected = [0, 1, 2, 3]
        self.assertEqual(all_v, expected)

    def test_get_node(self):
        in_node = self.graph.get_node(1)
        not_in_node = self.graph.get_node(10)
        expected_node_id = 1
        self.assertEqual(in_node.get_node_id(), expected_node_id)
        self.assertEqual(not_in_node, None)

    def test_all_in_edges_of_node_and_all_out_edges(self):
        all_in = list(self.graph.all_in_edges_of_node(1))
        expected = [0, 3]
        self.assertEqual(all_in, expected)
        all_out = list(self.graph.all_out_edges_of_node(1))
        expected = [0, 2]
        self.assertEqual(all_out, expected)

    def test_has_edge(self):
        check_edge = self.graph.has_edge(0, 1)
        self.assertEqual(check_edge, True)
        check_edge = self.graph.has_edge(2, 1)
        self.assertEqual(check_edge, False)

    def test_add_edge_and_remove_edge(self):
        self.graph.add_edge(1,3,1)
        size = self.graph.e_size()
        expected = 6
        self.assertEqual(size, expected)
        self.graph.remove_edge(1, 3)
        size = self.graph.e_size()
        expected = 5
        self.assertEqual(size, expected)

    def test_add_node_and_remove_node(self):
        self.graph.add_node(4)
        size = self.graph.v_size()
        expected = 5
        self.assertEqual(size, expected)
        self.graph.remove_node(4)
        size = self.graph.v_size()
        expected = 4
        self.assertEqual(size, expected)


if __name__ == '__main__':
    unittest.main()
