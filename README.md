# treeclust
[![Build Status](https://travis-ci.org/scwatts/treeclust.svg?branch=master)](https://travis-ci.org/scwatts/treeclust)
[![Code Coverage](https://codecov.io/gh/scwatts/treeclust/branch/master/graph/badge.svg)](https://codecov.io/gh/scwatts/treeclust)
[![License](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)


## Table of contents
* [Table of contents](#table-of-contents)
* [Introduction](#introduction)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [License](#license)


## Introduction
Calculating cophenetic pairwise tip distances from phylogenies can be slow. `treeclust` provides tools to quickly determine
distances, perform hierarchical cluster, and membership assignment.


## Requirements
There are a couple of software dependencies that are required:
* `Python`, version 3.6 or above
* `Biopython`, version 1.63 or above
* `gcc`, version 4.8.2 or above
* `gfortran`, version 4.8.2 or above


## Installation
Recommended method of installation is via pip:
```bash
pip3 install --user git+https://github.com/scwatts/treeclust.git
```


## Usage
```python
import pathlib
import Bio.Phylo.NewickIO
import treeclust

# Read in tree, assuming only single tree in file
input_phylo_fp = pathlib.Path('my_phylo.txt')
with input_phylo_fp.open('r') as fh:
    tree = next(Bio.Phylo.NewickIO.parse(fh))

# Run pairwise distance calculation and get clusters
distances, tips = treeclust.copheneticd(tree)
clustering = treeclust.hclust(distances, tree.count_terminals(), 3)

# Assign tip membership by cutting clustering dendrogram at a specific height
membership = treeclust.cuttree(clustering, 1.5)
```


## License
[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)
