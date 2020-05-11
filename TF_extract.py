#!/usr/bin/env python3

import sys


for gene_list in sys.argv[1:]:

#open all files that are needed
#metadata is the original metadatafile with all info
#juv_data is the juvenile metadata file with the clustering I want to maintain
#first, I am creating a dictionary where I store all the data in the metadata
	with open(gene_list, 'r') as metadata, open("TF_accession_numbers.txt", 'r') as juv_data, open("outputfile.txt", 'w') as outputfile:
		cell_list = []
		mydict = {}
		for line in metadata:
			line = line.rstrip()
			line_list = line.split('\t')
			mydict[line_list[0]] = line_list

#now that I have everything stored in a dictionary, I will
#iterate through the juv_data line by line. 
#eliminate the '\t' symbol
#the key is the first column in the juv_data. 
#if the key is in the juv_data line, then the dictionary key is
#replaced by the item.
		for item in juv_data:
			item = item.rstrip()
			item = item.split('\t')
			for key in mydict:
				if key in item:
					mydict[key] = item

#now we are writing ebverything to an output file
		for key in mydict:
			outputfile.write('\t'.join(mydict[key])+'\n')




	






			






