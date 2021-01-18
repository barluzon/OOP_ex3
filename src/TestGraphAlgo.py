import unittest
from unittest import TestCase
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):

    def test_get_graph(self):
        graph = DiGraph()
        for i in range(0, 3):
            graph.add_node(i)
        graph_algo = GraphAlgo(graph)
        self.assertEqual(graph_algo.get_graph(), graph)

    def test_load_and_save(self):
        graph = DiGraph()
        for i in range(0, 3):
            graph.add_node(i)
        graph.add_edge(0, 1, 1)
        graph.add_edge(1, 0, 1)
        graph.add_edge(1, 2, 2)
        graph.add_edge(2, 3, 3)
        graph.add_edge(3, 0, 4)
        graph_algo = GraphAlgo(graph)
        check = graph_algo.save_to_json(r'..\data\gen_graph')
        self.assertTrue(check)
        flag = graph_algo.load_from_json(r'..\data\gen_graph')
        self.assertTrue(flag)

    def test_shortest_path(self):
        graph = DiGraph()
        graph_algo = GraphAlgo(graph)

        for i in range(0, 11):
            graph.add_node(i)

        graph.add_edge(1, 2, 1)
        graph.add_edge(2, 3, 1)
        graph.add_edge(3, 4, 1)
        graph.add_edge(4, 5, 1)
        graph.add_edge(5, 10, 1)

        graph.add_edge(1, 6, 10)
        graph.add_edge(6, 7, 20)
        graph.add_edge(7, 8, 30)
        graph.add_edge(8, 9, 40)
        graph.add_edge(9, 10, 50)

        check = (float('inf'), [])
        check2 = (0, [0])
        check3 = (10, [1, 6])
        check4 = (5, [1, 2, 3, 4, 5, 10])
        self.assertEqual(graph_algo.shortest_path(2, 6), check)
        self.assertEqual(graph_algo.shortest_path(0, 0), check2)
        self.assertEqual(graph_algo.shortest_path(1, 6), check3)
        self.assertEqual(graph_algo.shortest_path(1, 10), check4)

    def test_connected_component(self):
        graph = DiGraph()
        graph_algo = GraphAlgo(graph)

        for i in range(0, 3):
            graph.add_node(i)

        graph.add_edge(0, 1, 1)
        graph.add_edge(1, 0, 1)
        graph.add_edge(1, 2, 1)
        graph.add_edge(2, 3, 1)
        graph.add_edge(3, 1, 1)

        check = [0, 1]
        self.assertEqual(graph_algo.connected_component(1), check)
        graph.remove_edge(0, 1)
        check2 = [1]
        self.assertEqual(graph_algo.connected_component(1), check2)

    def test_connected_components(self):
        graph = DiGraph()
        graph_algo = GraphAlgo(graph)

        for i in range(0, 3):
            graph.add_node(i)

        graph.add_edge(0, 1, 1)
        graph.add_edge(1, 0, 1)
        graph.add_edge(1, 2, 1)
        graph.add_edge(2, 3, 1)
        graph.add_edge(3, 1, 1)

        check = [[0, 1], [2]]
        self.assertEqual(graph_algo.connected_components(), check)

        graph.add_edge(3,2,1)
        graph.add_edge(2,1,1)

        check2 = [[0, 1, 2]]
        self.assertEqual(graph_algo.connected_components(), check2)

        graph.remove_edge(0,1)
        graph.remove_edge(3,1)

        check3 = [[0], [1, 2]]
        self.assertEqual(graph_algo.connected_components(), check3)

        graph.remove_edge(1,0)
        graph.remove_edge(1,2)
        graph.remove_edge(2,3)
        graph.remove_edge(3,2)

        check4 = [[0], [1], [2]]
        self.assertEqual(graph_algo.connected_components(), check4)

if __name__ == '__main__':
    unittest.main()
