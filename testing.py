#!/usr/bin/env python3
import argparse
import collections
import pathlib


import Bio.Phylo.NewickIO


import copheneticd


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_fp', required=True, type=pathlib.Path,
            help='Inptu file path pls')

    # Ensure that input file exists
    args = parser.parse_args()
    if not args.input_fp.exists():
        parser.error('Input file %s does not exist' % args.input_fp)

    return args


class Node():

    def __init__(self, tree_node, parent_id):
        self.parent_id = parent_id
        self.tree_node = tree_node
        self.branch_length = tree_node.branch_length


def main():
    # Get command line arguments
    args = get_arguments()

    # Read in tree, assuming only single tree in file
    with args.input_fp.open('r') as fh:
        tree = next(Bio.Phylo.NewickIO.parse(fh))

    # Get terminal and non-terminal nodes
    tips = tree.count_terminals()
    nodes = len(tree.get_nonterminals())

    # Get edges and distances
    distances, edges = edge_distances(tree, tips)

    # TODO: must apply cladewise ordering prior to cophenetic distance calc
    edges_source, edges_target = zip(*edges)
    flat_distances = copheneticd.run(tips, nodes, edges_source, edges_target, distances, len(edges))

    # Round to reasonable decimal places
    flat_distances = [round(d, 4) for d in flat_distances]

    # Create 2d list from distances
    row_gen = (flat_distances[i:i+tips] for i in range(0, len(flat_distances), tips))
    distances = [row for row in row_gen]
    for r in distances:
        print(*r, sep='\t')


def edge_distances(tree, tip_number):
    # Init ret vars
    distances = list()
    edges = list()

    # Add tree root to tree; dfs traversal
    # ape::cophenetic requires tip numbering to start from 0..(len(tips)-1) and internal nodes
    # to start from len(tips)..(len(elements)-1)
    node_i = tip_number
    tip_i = 0

    node_queue = collections.deque()
    node_queue.append(Node(tree.clade, None))
    while node_queue:
        # Get next node
        node = node_queue.pop()

        # Get node id
        if node.tree_node.is_terminal():
            node_id = tip_i
            tip_i += 1
        else:
            node_id = node_i
            node_i += 1

        # Record children
        for child_node in node.tree_node.clades[::-1]:
            node_queue.append(Node(child_node, node_id))

        # Skip node if it is root
        if node.branch_length is None:
            continue

        # Record distances and edges
        distances.append(node.branch_length)
        edges.append((node.parent_id, node_id))

    return distances, edges


if __name__ == '__main__':
    main()
