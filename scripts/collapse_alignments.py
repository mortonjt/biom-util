#!/USSR/bin/env python
import argparse
import biom
import biom.util import biom_open
import pandas as pd


def main(args):
    table = biom.load_table(args.table)
    aligns = pd.read_table(args.align, header=None)
    seq_to_genome = aligns[[0, 2]].set_index(0)
    bin_f = lambda x: seq_to_genome.loc[x]
    t = table.collapse(bin_f, norm=False, min_group_size=1,
                       axis='observation').sort(axis='observation')
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
