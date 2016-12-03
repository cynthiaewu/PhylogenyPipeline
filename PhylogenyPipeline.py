import sys
import subprocess
import operator

if len(sys.argv) != 3:
    print("ERROR: Incorrect number of arguments")
    print("USAGE: python PhylogenyPipeline.py [allsequences].fas [querysequences].fas")
    exit(-1)
    
# first command line argument: fasta file of all sequences
fastafile = sys.argv[1]
# second command line argument: fasta file of only query sequences
querySequences = sys.argv[2]
name = fastafile.rsplit(".", 1)
if name[1].upper() != "FAS" or name[1].upper() != "FASTA":
    print("ERROR: File isn't in corect fasta format")
    exit(-1)
subject = name[0]
trefile = subject + ".tre"
distancefile = subject + "matrix.txt"

allsequences = open("temp.fas", 'w')
queryfile = open(querySequences, 'r')
print("Reading query file")
#parse query fasta file to grab query sequences
query = set()
for line in queryfile:
    if line.startswith(">"):
        allsequences.write(line)
        l = line.rstrip()
        query.add(l[1:])
    else:
        allsequences.write(line)               
queryfile.close()
print("Query file read")

database = open(fastafile, "r")
for line in database :
    allsequences.write(line)
allsequences.close()
fastafile.close()

# run PASTA
work = subprocess.call(subprocess.call(["run_pasta.py", "-i", allsequences, "-j", subject]))
if  work != 0:
    print("ERROR: PASTA didn't run correctly")
    exit(-1)


# run newick-utils
f = open(distancefile, 'w')
work = subprocess.call(["nw_distance", "-n", "-m", "m", trefile], stdout=f)
if  work != 0:
    print("ERROR: Newick-utilities didn't run correctly")
    exit(-1)
print("Newick finished")
f.close()

matrix = open(distancefile, 'r')
print("Reading matrix file")
firstline = matrix.readline()
seq = firstline.split('\t')

found = {}
numberLines = 0
# store distances of query
for line in matrix:
    dis = line.split('\t')
    numberLines += 1
    if dis[0] in query :
        found[dis[0]] = dis
        
matrix.close()
print("Matrix file read")

# create a text file of pairwise distances for each query from the matrix file
for item in found :
    dict = {}
    for i in range(numberLines):
        dict[seq[i]] = found[item][i]
    
    # sort from closest distance to furthest 
    sorted_dict = sorted(dict.items(), key=operator.itemgetter(1))

    outfile = item + "phylogeny.txt"
    output = open(outfile, 'w')
    output.write("Sequence" + "\t" + "Distance" + "\n")
    for x in sorted_dict:
        output.write(x[0] + "\t" + x[1])
        output.write("\n")
    output.close()
    print(outfile + " created")
