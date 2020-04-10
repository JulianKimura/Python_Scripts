#!/usr/bin/env python3


'''
README: to use this script, type in the following in the command line: 
python3 removing_lines.py file_with_things_to_remove.txt original_file.txt

This script isn't the most efficient thing in the world, but it works. 
If things seeem to take too long, consider moving this to the cluster
and run it as part of a bash script!! I think when I ran this script it took
a couple hours.... but it got the job done. This script is a computer scientist's
nightmare.  
'''

import sys
import re



with open(sys.argv[1], 'r') as genes, open(sys.argv[2], 'r') as ogfile,  open('outputfile.txt', 'w') as outputfile:
	gene_list = []
	for line in genes:
		line = line.rstrip()
		gene_list.append(line)

	line_list = []
	for line in ogfile:
		line = line.rstrip()
		line_list.append(line)

	final_list = []
	for line in line_list:
		for item in gene_list:
			if re.search(rf"{item}", line):
				final_list.append(line)

	for line in final_list:
		for item in line_list:
			if line in item:
				line_list.remove(item)

	for line in line_list:
		outputfile.write(line+'\n')

