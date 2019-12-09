#!/usr/bin/env python3

import sys
import re

num_reads_list = []
file_number = 0
mydict = {}
with open('combined_counts.txt', 'w') as outputfile:
	for files in sys.argv[1:]:
		file_number+=1
		gene_name_list = []
		with open(files, 'r') as inputfile:
			for line in inputfile:
				line = line.rstrip()
				if re.search(r"\|", line):
					line_list = line.split('\t')
					gene_name_list.append(line_list[0])
					num_reads_list.append(line_list[1])
		mydict['gene_names'] = gene_name_list
		mydict[files+str(file_number)] = num_reads_list

#adds the header
	for index in mydict:
		outputfile.write(index+'\t')
	outputfile.write('\n')
#looping through the indices 
	for x in range(len(mydict['gene_names'])):
		for index in mydict:
			outputfile.write(mydict[index][x])
			outputfile.write('\t')
		outputfile.write('\n')


with open('combined_counts.txt', 'r') as inputfile, open('combined_counts_filtered.txt', 'w') as output2:
	for line in inputfile:
		line = line.rstrip()
		if "gene_names" in line:
			output2.write(line+'\n')
		if re.search(r"\|", line):
			line_list = line.split('\t')
			count_list = line_list[1:file_number+1]
			floated_count_list = [float(item) for item in count_list]
			if sum(floated_count_list) != 0:
				output2.write(line+'\n')

