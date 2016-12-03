README
--------------------------------------------------------------------------------
The phylogeny pipeline runs PASTA and Newick Utilities to return a pairwise 
distance file for each query sequence, showing the sequence similarities between
each query (the “unknowns”) and all provided known sequences.

Documentation: in addition to this README file, you can consult our detailed 
Tutorial write-up on the uses, project pipeline, and biological relevance of the
project.

--------------------------------------------------------------------------------
INSTALLATION
--------------------------------------------------------------------------------
Dependencies:
You need to have python 3.5 installed.
You need to have java installed.

Download the following two tools, preferably in the PATH variable 
(or alternatively in the folder containing the query files to be run):

PASTA (Practical Alignment using Sate and TrAnsitivity)
Follow the installation instructions on the github: 
https://github.com/smirarab/pasta
This tool with create a more accurate sequence alignment and maximum likelihood
tree after several iterations.

Newick Utilities
Download version 1.6.0 of the binaries 
(i.e. newick-utils-1.6-Linux-x86_64-disabled-extra.tar.gz) 
from http://cegg.unige.ch/newick_utils

--------------------------------------------------------------------------------
EXECUTION
--------------------------------------------------------------------------------
To test the phylogeny pipeline

1. Cd into the folder with the TestData.fas and TestQuery.fas
2. From command line, run this command:

python PhylogenyPipeline.py TestData.fas TestQuery.fas

To run the phylogeny pipeline in the command line: 

Command line: python PhylogenyPipeline.py $arg1 $arg2
	arg1: name of fastafile with all the sequences including query sequence(s)
	arg2: name of fastafile with only the query sequence(s)

OPTION: View PASTA tree in Figtree
	    Available to download at http://tree.bio.ed.ac.uk/software/figtree/

--------------------------------------------------------------------------------
OUTPUT
--------------------------------------------------------------------------------
1. Tree file (from PASTA) - [jobname].tre
2. Alignment file (from PASTA) - [jobname]_temp_iteration_2_seq_alignment.txt
3. Text files of pairwise distances (closest to furthest) for each query sequences.
[jobname]phylogeny.text. Multiple query sequences will create multiple text files
