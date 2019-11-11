#!/usr/bin/env python3

#this script will read in two files through the command line. the first file will contain the genes of interest. the second file will contain information of interest along with genes. the genes of interest must be the first column in the table. This script will take csv or tab delimited formatting for the file containing the gene of interest

import sys
import re

#specifies the input from the command line
testfile = sys.argv[1]
testfile2 = sys.argv[2]

#opens the first file that is inputted next to the script on the command line
with open(testfile, 'r') as input_file:
#creates an empty list where the gene names present in the file will be stored in
	gene_list = []
#for every line in the input file, the new line character is deleted, and if the line contains a pipe symbol, it will eliminate all quotes and commas (common in csv files), and will delete all characters following the pipe symbol. the resulting line will then be stored into the empty list that was created earlier
	for line in input_file:
		line = line.rstrip()
		if re.search(r"\|", line):
			line = re.sub(r"\"", "", line)
			line = re.sub(r"\,", "", line)
			line = re.sub(r"\|.+", "", line)
			gene_list.append(line)
		else:
			continue
#opens the second file on the command line as well as creates a new file called output file. if the gene name stored in the list is found in the second file, the script will print that particular line in the output file. 
with open(testfile2, 'r') as new_file, open('outputfile.txt', 'w') as output_file:
	for line in new_file:
		for gene in gene_list:
			if gene in line:
				output_file.write(line+'\n')


