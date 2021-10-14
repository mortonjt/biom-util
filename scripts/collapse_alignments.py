#!/USSR/bin/env python
import argparse
import biom
from biom.util import biom_open
import numpy as np
import pandas as pd
from scipy.sparse import coo_matrix
import scipy as sp


def main(args):
    table = biom.load_table(args.table)
    aligns = pd.read_table(args.align, header=None)
    seq_to_genome = aligns[[0, 2, 4]].groupby(by=[0]).min()[2]
    ids = list(set(seq_to_genome.index) & set(table.ids(axis='observation')))
    t = table.filter(ids, axis='observation')
    bin_f = lambda i, x: seq_to_genome.loc[i]
    t = t.collapse(bin_f, norm=False, min_group_size=1, axis='observation')
    #t = groupby_sum(t, seq_to_genome)
    with biom_open(args.output_table, 'w') as f:
        t.to_hdf5(f, 'collapsed')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('--table', type=str, required=True,
                        help='Path to biom table.')
    parser.add_argument('--align', type=str, required=True,
                        help='Path to sam alignments.')
    parser.add_argument('--output-table', type=str, required=True,
                        help='Path to output fasta file.')
    args = parser.parse_args()
    main(args)
