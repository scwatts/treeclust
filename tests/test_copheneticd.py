#!/usr/bin/env python3
import unittest


import Bio.Phylo.NewickIO


import copheneticd


class TestCopheneticd(unittest.TestCase):

    def test_small_tree(self):
        tree_fp = 'data/small_random_tree.txt'
        with open(tree_fp, 'r') as fh:
            tree = next(Bio.Phylo.NewickIO.parse(fh))

        result = [[0.0, 1.9205948539000002, 2.3202793119000003, 3.0886009296, 3.0198757022000002],
                  [1.9205948539000002, 0.0, 1.2080715858, 3.2276288861, 3.1589036587000003],
                  [2.3202793119000003, 1.2080715858, 0.0, 3.6273133441, 3.5585881167],
                  [3.0886009296, 3.2276288861, 3.6273133441, 0.0, 1.6179366946],
                  [3.0198757022000002, 3.1589036587000003, 3.5585881167, 1.6179366946, 0.0]]
        self.assertEqual(copheneticd.distance(tree), result)
