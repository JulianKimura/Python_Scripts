#!/usr/bin/env python3

#this script will read in two files through the command line. the first file will contain the genes of interest. the second file will contain information of interest along with genes. the genes of interest must be the first column in the table. This script will take csv or tab delimited formatting for the file containing the gene of interest

import sys
import re

'''
#specifies the input from the command line
transposed_counts = sys.argv[1]

#opens the first file that is inputted next to the script on the command line
with open(transposed_counts, 'r') as input_file, open('cell_list.txt', 'w') as intermediatefile:
#creates an empty list where the gene names present in the file will be stored in
#creates a file called cell_list.txt which is a list of all of the cell names 	
	for line in input_file:
		line = line.rstrip()
		line_list = line.split('\t')
		intermediatefile.write(line_list[0]+'\n')
'''

#open the newly made cell_list.txt file and the original metadatafile

ogmetadata = sys.argv[1]
with open('cell_list.txt', 'r') as cell_list, open(ogmetadata, 'r') as new_file,  open('subsetted_metadata.txt', 'w') as outputfile:
	list1 = []
	for line in cell_list:
		line = line.rstrip()
		list1.append(line)

	for line in new_file:
		for item in list1:
			if item in line:
				outputfile.write(line)


'''
	[lines[k] for k in range(len(new_file) for i in range(len(list1)) if list1[i] in lines[k]]
'''

'''
			if list1[i] in line:
'''	
'''
				outputfile.write(line+'\n')
'''

