#!/usr/bin/env python3
import argparse
import pathlib


import Bio.Phylo.NewickIO


import treeclust


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_fp', required=True, type=pathlib.Path,
            help='Input newick-format tree file path')

    # Ensure that input file exists
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

    # Run pair-wise-distance calculation
    distances, tips = treeclust.copheneticd(tree)

    # Get clusters
    clustering = treeclust.hclust(distances, tree.count_terminals(), 3)

    # Cut the tree
    membership = treeclust.cuttree(clustering, 1.5)


if __name__ == '__main__':
    main()
