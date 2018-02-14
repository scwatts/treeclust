import collections
import sys


import Bio.Phylo


import _treeclust


class Node():

    def __init__(self, tree_node, parent_id):
        self.parent_id = parent_id
        self.tree_node = tree_node
        self.branch_length = tree_node.branch_length


def copheneticd(tree):
    # Check that input tree is an instance of BioPython's BaseTree
    if not isinstance(tree, Bio.Phylo.BaseTree.Tree):
        print('error: recived non-tree object', file=sys.stderr)
        return

    # Get terminal and non-terminal nodes
    tips = tree.count_terminals()
    nodes = len(tree.get_nonterminals())

    # Get edges and distances
    distances, edges, ordered_tips = edge_distances(tree, tips)

    # TODO: must apply cladewise ordering prior to cophenetic distance calc
    # TODO: this may not be necessary for raw trees
    edges_source, edges_target = zip(*edges)
    result = _treeclust.copheneticd(tips, nodes, edges_source, edges_target, distances, len(edges))
    return result, ordered_tips


def edge_distances(tree, tip_number):
    # Init ret vars
    distances = list()
    edges = list()
    tip_order = list()

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
            # Record tip and tip number so we can return ordered list
            tip_order.append((node.tree_node.name, tip_i))
        else:
            node_id = node_i
            node_i += 1

        # Record children
        for child_node in node.tree_node.clades[::-1]:
            node_queue.append(Node(child_node, node_id))

        # Skip node if it is root
        if node.branch_length is None:
            continue

        # Record data
        distances.append(node.branch_length)
        edges.append((node.parent_id, node_id))

    ordered_tips = [name for name, i in sorted(tip_order, key=lambda k: k[1])]
    return distances, edges, ordered_tips


def hclust(distances, elements, method):
    # TODO: add handler for options to take as string
    # TODO: logic to determine or take number of elements
    # TODO: check arguments have a valid configuration
    return _treeclust.hclust(distances, elements, method)


def cuttree(tree, height_threshold):
    # TODO: check arguments have a valid configuration
    n = len(tree['order'])
    for i, height in enumerate(tree['height'], 1):
        if height > height_threshold:
            k = n - i + 1
            break
    else:
        k = n - i

    return _treeclust.cuttree(tree['merge'], k, n)
