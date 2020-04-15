import argparse

#USAGE: For default read splitting in half only one argument is needed: 
#	python cleave.py -in <input-file>



#We create the input and output objects
parser = argparse.ArgumentParser()
parser.add_argument('-in', action="store", dest = 'input')
parser.add_argument('-out', action="store", dest = 'output_1')
parser.add_argument('-m', action="store", dest = 'mode', default='split')

args = parser.parse_args()

i = 1
f1 = open(str(args.input), 'r')

#Output files
basename =str(args.input).split('.fastq')[0]
forward=basename+'_1.fq'
reverse=basename+'_2.fq'

f2_1 = open(forward, 'w')
f2_2 = open(reverse, 'w')

if args.mode == "split":
	for line in f1:
		if i == 1:
			name = str(line).strip('\n')

		if i == 2: 
			half = len(line)/2
			full = len(line)+1
			seq1= str(line)[0:half].strip('\n')
			seq2= str(line)[half:full].strip('\n')

		if i == 3:
			pass

		if i == 4:
			qual1= str(line)[0:half].strip('\n')
			qual2= str(line)[half:full].strip('\n')

			f2_1.write(name+'.1'+  '\n' + seq1 + '\n' + '+' + '\n' + qual1 + '\n' )
                        f2_2.write(name+'.2'+  '\n' + seq2 + '\n' + '+' + '\n' + qual2 + '\n' )

			i = 0

		i = i + 1


if args.mode == "trim":
	for line in f1:
		if i == 1:
			name = str(line).strip('\n')

		if i == 2: 
			seq1= str(line)[6:51].strip('\n')

		if i == 3:
			pass

		if i == 4:
			qual1= str(line)[6:51].strip('\n')

			f2.write(name+'.1'+  '\n' + seq1 + '\n' + '+' + '\n' + qual1 + '\n')
			i = 0

		i = i + 1
