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

#extract from a to b to a new file

chromosome="3"
a="15094267"
b="15096967"

t  = open("out_crop_2.fa", "w")
with open("ler.fa") as fp:
	for name, seq in read_fasta(fp):
		if chromosome in name.lower():
			t.write(name + '\n' + seq[int(a):int(b)] + '\n')

t.close()
