# biom-util
Random utility scripts for manipulating biom tables

# Installation

This repository can be installed via 
```
pip install git+https://github.com/mortonjt/biom-util
```

For aligning sequencing, you may also need to install bowtie2, which can be installed via

```
conda install -c bioconda bowtie2
```

# Basic usage

There are 3 scripts

`extract_seqs.py` : extracts reas directly from biom file.  This assumes that denoised themselves are used as the observation ids

`align_seqs.py` : uses bowtie2 to map denoised reads to a prebuilt bowtie database of reference genomes

`collapse_alignments.py` : collapses the denoised biom table to corresponding reference genomes as determined by `align_seqs.py`

Use the `--help` option to see the options for each of these commands.

## Help menu
```
usage: extract_seqs.py [-h] --table TABLE --output-fasta OUTPUT_FASTA

optional arguments:
  -h, --help            show this help message and exit
  --table TABLE         Path to biom table.
  --output-fasta OUTPUT_FASTA
                        Path to output fasta file.
```                        

```
usage: align_seqs.py [-h] --seqs SEQS --align ALIGN --database DATABASE [--nprocs NPROCS]

optional arguments:
  -h, --help           show this help message and exit
  --seqs SEQS          Path to fasta file.
  --align ALIGN        Path to output sam alignments.
  --database DATABASE  Path to bowtie database to align against.
  --nprocs NPROCS      Number of processors to run.
```

```
usage: collapse_alignments.py [-h] --table TABLE --align ALIGN --output-table OUTPUT_TABLE

optional arguments:
  -h, --help            show this help message and exit
  --table TABLE         Path to biom table.
  --align ALIGN         Path to sam alignments.
  --output-table OUTPUT_TABLE
                        Path to output fasta file.
```

## Examples

```
extract_seqs.py --table all.biom --output-fasta all.seqs.fa
```

```
align_seqs.py --seqs all.seqs.fa --align all.seqs.sam --database wol/databases/bowtie2/WoLr1 --nprocs 8
```

```
collapse_alignments.py --table all.biom --align all.seqs.sam --output-table all.wol.biom
```

## Notes
If you are using the Web of Life database, you'll need to download all of the corresponding files.  See [here](https://biocore.github.io/wol/data/) for more information.
