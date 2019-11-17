#!usr/bin/env python3
import sys
import re
file_typed = sys.argv[1]

#takes in file that is inputted on command line
with open(file_typed, 'r') as input_file, open('output.txt','w') as outputfile:
#for every line in the input file, eliminates the new line symbol
#for every line in the input file, resets a item_list
	for line in input_file:
		line = line.rstrip()
		item_list = []
#if the line contains a hofstenia id, it will treat it as a non-title and do the following
		if re.search(r'^9', line):
#creates a list of the line
			line_list = line.split('\t')
#eliminates the items on the list that is the hofstenia id
#stores the hofstenia id as a string called line_id
			line_id = line_list[0]
			line_list.pop(0)
#for every item in the list, turn it into a float and if the item is less than or equal to 0.05, adds to the item_list defined above
			for item in line_list:
				item = float(item)
				if item <= 0.05:
					item_list.append(item)
#if the item_list contains at least a single item, the list_id or the hofstenia id that was associated with the line is written into the output file.
			if bool(item_list) == True:
				outputfile.write(line_id+'\n')
#if the line does not contain a hofstenia id, then continue and do not do anything specified above. 
		else:
			continue	
