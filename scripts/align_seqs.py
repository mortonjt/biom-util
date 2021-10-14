#!/usr/bin/env python

import argparse
import subprocess


def main(args):
    cmd = (
        f'bowtie2 -x {args.database}'
        f' -p {args.nprocs} -f {args.seqs} -S {args.align}'
        " -k 16 --np 1 --mp 1,1 --rdg 0,1 --rfg 0,1"
        " --score-min L,0,-0.05 --very-sensitive --no-head --no-unal"
    )
    proc = subprocess.Popen(cmd, shell=True)
    proc.wait()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('--seqs', type=str, required=True,
                        help='Path to fasta file.')
    parser.add_argument('--align', type=str, required=True,
                        help='Path to output sam alignments.')
    parser.add_argument('--database', type=str, required=True,
                        help='Path to bowtie database to align against.')
    parser.add_argument('--nprocs', type=int, required=False, default=8,
                        help='Number of processors to run.')
    args = parser.parse_args()
    main(args)
