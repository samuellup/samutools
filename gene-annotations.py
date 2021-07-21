# This script was made to add annotations to a gene listo from a plain text file, the TAIR10_gene_info.txt input  
# was modified to avoid empty columns by adding "-" characters. 

import argparse

# Parse command arguments
parser = argparse.ArgumentParser()
parser.add_argument('-in', action="store", dest='input', required=True)
parser.add_argument('-out', action="store", dest='output', required=True)
parser.add_argument('-ann', action="store", dest='ann')

args = parser.parse_args()

output = open(args.output, "a+")

with open(args.input, "r") as infile: 
    for line in infile: 
        if not line.startswith("Log"):
            gene_id = line.split()[3]
            with open(args.ann, "r") as annotation: 
                for l in annotation: 
                    if l.split()[0] == gene_id: 
                        gene_name = l.split("\t")[1]
                        gene_class = l.split("\t")[2]
                        if gene_class == "0": gene_class = "-"
                        description = l.split("\t")[4]
                        break
            output.write(line.strip() + "\t" + gene_name + "\t" + gene_class + "\t" + description + "\n" )

