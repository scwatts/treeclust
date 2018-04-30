#!/usr/bin/env python3
import argparse
import pathlib

import Bio.Phylo.NewickIO
import treeclust


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_fp', required=True, type=pathlib.Path,
            help='Input newick phylogeny filepath')

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

    # Run pairwise distance calculation and report
    distances, tips = treeclust.copheneticd(tree)
    print('tip_labels', *tips, sep='\t')
    for i in range(len(tips)):
        print(tips[i], end='\t')
        for j in range(len(tips)):
            if i == j:
                print('\t0.0000', end='')
            else:
                index = get_index(i, j, len(tips)) if i > j else get_index(j, i, len(tips))
                distance_string = '{:0.4f}'.format(distances[index])
                print('\t', distance_string, sep='', end='')
        print()


def get_index(i, j, n):
    '''Map subscript indices to linear indices for square matrices with no diagonal.

    Argument i must be greater than j. Argument n is number of row (or column) elements'''
    return (i - 1) + j * (n - 1) - ((j + 1) * j) // 2


if __name__ == '__main__':
    main()
