#!/usr/bin/env python3
import argparse
import pathlib


import Bio.Phylo.NewickIO
import treeclust


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_fp', required=True, type=pathlib.Path,
            help='Input newick-format tree file path')

    args = parser.parse_args()
    if not args.input_fp.exists():
        parser.error('Input file %s does not exist' % args.input_fp)

    return args


def main():
    # Get command line arguments
    args = get_arguments()

    # Read in tree, assuming only single tree in file
    with args.input_fp.open('r') as fh:
        tree = next(Bio.Phylo.NewickIO.parse(fh))

    # Run pairwise distance calculation and get clusters
    distances, tips = treeclust.copheneticd(tree)
    clustering = treeclust.hclust(distances, tree.count_terminals(), 3)

    # Assign tip membership by cutting clustering dendrogram at a specific height
    membership = dict()
    for tip, m in zip(tips, treeclust.cuttree(clustering, 1.5)):
        try:
            membership[m].append(tip)
        except KeyError:
            membership[m] = [tip]

if __name__ == '__main__':
    main()
