#!/usr/bin/env python
import argparse
import biom


def main(args):
    table = biom.load_table(args.table)
    ids = table.ids(axis='observation')
    with open('seqs.fa', 'w') as f:
       f.write('\n'.join(list(map(lambda x: f'>{x}\n{x}', ids))))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('--table', type=str, required=True,
                        help='Path to biom table.')
    parser.add_argument('--output-fasta', type=str, required=True,
                        help='Path to output fasta file.')
    args = parser.parse_args()
    main(args)
