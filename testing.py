#!/usr/bin/env python3
import _treeclust


def main():
    distances = [1.920595, 2.320279, 3.088601, 3.019876, 1.208072, 3.227629, 3.158904, 3.627313, 3.558588, 1.617937]
    print(_treeclust.hclust(distances, 5, 3))


if __name__ == '__main__':
    main()
