#!/usr/bin/env python3
import unittest


import Bio.Phylo.NewickIO


import treeclust


class TestTreeclust(unittest.TestCase):


    def setUp(self):
        self.tree = self.load_tree()
        self.distances = treeclust.copheneticd(self.tree)
        # TODO: update parameters once we have some more logic for element determination
        self.clustering = treeclust.hclust(self.distances, 5, 3)
        self.membership = treeclust.cuttree(self.clustering, 1.5)

    @staticmethod
    def load_tree():
        tree_fp = 'data/small_random_tree.txt'
        with open(tree_fp, 'r') as fh:
            return next(Bio.Phylo.NewickIO.parse(fh))

    def test_small_tree_copheneticd(self):
        expected_result = [1.9205948539000002,
                           2.3202793119000003, 3.0886009296,
                           3.0198757022000002, 1.2080715858, 3.2276288861,
                           3.1589036587000003, 3.6273133441, 3.5585881167, 1.6179366946]
        self.assertEqual(self.distances, expected_result)

    def test_small_tree_hclust(self):
        expected_result = {'merge': [[-2, -3], [-4, -5], [-1, 1], [2, 3]],
                           'height': [1.2080715858, 1.6179366946, 2.3202793119000003, 3.6273133441],
                           'order': [4, 5, 1, 2, 3]}
        self.assertEqual(self.clustering, expected_result)

    def test_small_tree_cuttree(self):
        expected_result = [1, 2, 2, 3, 4]
        self.assertEqual(self.membership, expected_result)
