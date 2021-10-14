# biom-util
Random utility scripts for manipulating biom tables

There are 3 scripts

`extract_seqs.py` : extracts reas directly from biom file.  This assumes that denoised themselves are used as the observation ids

`align_seqs.py` : uses bowtie2 to map denoised reads to a prebuilt bowtie database of reference genomes

`collapse_alignments.py` : collapses the denoised biom table to corresponding reference genomes as determined by `align_seqs.py`
