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
You need to have python 3.5 and java installed.

Download the following two tools, preferably in the PATH variable 
(or alternatively in the folder containing the query files to be run):

PASTA (Practical Alignment using Sate and TrAnsitivity) -- 
Follow the installation instructions on the github: 
https://github.com/smirarab/pasta
This tool with create a more accurate sequence alignment and maximum likelihood
tree after several iterations.

Newick Utilities -- 
Download version 1.6.0 of the binaries 
(i.e. newick-utils-1.6-Linux-x86_64-disabled-extra.tar.gz) 
from http://cegg.unige.ch/newick_utils

--------------------------------------------------------------------------------
INPUT
--------------------------------------------------------------------------------
Limitation: The sequence headers of fasta file cannot have any spaces.



1. dataset of all sequences excluding query sequences in fasta file

   [allsequences].fas
   
2. query sequences in fasta file

   [querysequences].fas
   
--------------------------------------------------------------------------------
EXECUTION
--------------------------------------------------------------------------------

Running a test job: to test the phylogeny pipeline using the command line,

1. Cd into the folder with the TestData.fas and TestQuery.fas
2. From command line, run this command:

 ```
 python PhylogenyPipeline.py TestData_Avian_Swine_Human_flu.fas TestQuery_Flu.fas 
 ```
If the phylogeny pipeline runs successfully, it will produce all of the output files
listed in the next section.

To run the phylogeny pipeline on sequences of interest: 

Type into the command line:

	python PhylogenyPipeline.py $arg1 $arg2

	arg1: name of the fastafile containing all the sequences excluding query sequence(s)
	arg2: name of the fastafile containing the query sequence(s)

--------------------------------------------------------------------------------
OUTPUT
--------------------------------------------------------------------------------

All final output files of interest are located in a folder titled
[allsequences]_PhylogenyOutput:

1. Maximum likelihood tree file (generated by PASTA) - [allsequences].tre
2. Sequence alignment file (generated by PASTA) - [allsequences]_aligned.txt
3. Text file containing pairwise distances (closest to furthest) for query sequence
compared to each of the known sequences - [queryID]_phylogeny_distance.txt
Each query sequence will produce its own distance text file.

OPTION: Maximum likelihood tree can be viewed in Figtree
(http://tree.bio.ed.ac.uk/software/figtree/) or other software.
Alignments can be viewed in text editor programs or applications such as Seaview
(http://doua.prabi.fr/software/seaview).

The PASTA step of this program will also produce many temporary and other files,
which are detailed in the PASTA tutorial (https://github.com/smirarab/pasta/blob/master/pasta-doc/pasta-tutorial.md),
but for the purposes of our phylogeny pipeline, we focus on the output files placed
into the PhylogenyOutput folder.
