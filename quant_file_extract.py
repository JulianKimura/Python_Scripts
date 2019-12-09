#!/usr/bin/env python3

import sys
quant_file = sys.argv[1:]

with open(quant_file, 'r') as inputfile, open('count_file.txt', 'w') as outputfile:
	for line in inputfile:
		line = line.rstrip()
		line_list = line.split('\t')
		gene_name = line_list[0]
		num_reads = line_list[4]
		outputfile.write(gene_name+'\t'+num_reads+'\n')


