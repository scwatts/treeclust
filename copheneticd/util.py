import collections
import sys


import Bio.Phylo


import _copheneticd


class Node():

    def __init__(self, tree_node, parent_id):
        self.parent_id = parent_id
        self.tree_node = tree_node
        self.branch_length = tree_node.branch_length


def distance(tree):
    # Check that input tree is an instance of BioPython's BaseTree
    if not isinstance(tree, Bio.Phylo.BaseTree.Tree):
        print('error: recived non-tree object', file=sys.stderr)
        return

    # Get terminal and non-terminal nodes
    tips = tree.count_terminals()
    nodes = len(tree.get_nonterminals())

    # Get edges and distances
    distances, edges = edge_distances(tree, tips)

    # TODO: must apply cladewise ordering prior to cophenetic distance calc
    edges_source, edges_target = zip(*edges)
    flat_distances = _copheneticd.run(tips, nodes, edges_source, edges_target, distances, len(edges))

    # TODO: see if ther is some alternative in native c; this is very expensive
    # Round to reasonable decimal places
    flat_distances = [round(d, 6) for d in flat_distances]

    # Create 2d list from distances
    row_gen = (flat_distances[i:i+tips] for i in range(0, len(flat_distances), tips))
    return [row for row in row_gen]


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
