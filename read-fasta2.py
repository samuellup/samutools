# Function to parse fasta file (based on one of the Biopython IOs)
def read_fasta(fp):
	name, seq = None, []
	for line in fp:
		line = line.rstrip()
		if line.startswith('>'):
			if name: yield (name, ''.join(seq))
			name, seq = line, []
		else:
			seq.append(line)
	if name: yield (name, ''.join(seq))

#Searches string in fasta name, writes hits in output file
string = "POTATO"

t  = open("out_potato.txt", "w")
with open("in.fa") as fp:
	for name, seq in read_fasta(fp):
		if string in name.lower():
			t.write(name + '\n' + seq + '\n')

t.close()
