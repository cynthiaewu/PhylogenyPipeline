import sys
import subprocess
import operator

# first command line argument: fasta file of all sequences, including query
fastafile = sys.argv[1]
# second command line argument: fasta file of only query sequences
querySequences = sys.argv[2]
name = fastafile.rsplit(".", 1)
subject = name[0]
trefile = subject + ".tre"
distancefile = subject + "matrix.txt"

queryfile = open(querySequences, 'r')
print("Reading query file")
#parse query fasta file to grab query sequences
query = set()
for line in queryfile:
    if line.startswith(">"):
                query.add(line[1:len(line)-1])
queryfile.close()
print("Query file read")

# run PASTA
subprocess.call(["run_pasta.py", "-i", fastafile, "-j", subject])

# run newick-utils
f = open(distancefile, 'w')
subprocess.call(["nw_distance", "-n", "-m", "m", trefile], stdout=f)
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
