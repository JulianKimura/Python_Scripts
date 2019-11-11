#!/usr/bin/env python3
import re
import sys

#this script will take in any number of csv or tab delimited format, as long as the first column contains all of the gene IDs in the format of our hofstenia transcriptome. i.e. "98xxxxx|gene-xxx" and will create a text file with a single column that is ready to be placed into DAVID for GO analysis


#setting error messages
try:
	x = sys.argv[1]
except IndexError:
	print("Looks like you didn't provide a file to convert!\nTry typing 'python3 GO_conversion.py file1 file2 etc.....' on the command line")

#for every file written on the command line next to the name of the script
for files in sys.argv[1:]:
#open the files, and create an output file that has the word GO at the begining of it
	with open(files, 'r') as input_file, open('GO'+files+'.txt', 'w') as output_file:
#for each of the lines in the input files that are opened
		for line in input_file:
#eliminate all line break characters
#if the line contains an unknown, then skip.
			line = line.rstrip()
			if 'unknown' in line:
				continue
#if the line contains a pipe, do the following
			if re.search(r"\|", line):
#eliminate all quotations in the line:
				line = re.sub(r"\"", "", line)
#substitute all characters before and including the capital X with nothing
				line = re.sub(r".+\|","",line)
#substitute all characters after the "-" with nothing
				line = re.sub(r"-.+","",line)
#eliminate all commas if this is a csv file
				line = re.sub(r"\,.+","",line)
#eliminate everything after a tab space in a tab delimited text
				line = re.sub(r"\t.+","",line)
#capitalize all characters in the line
				line = line.upper()			
#append the string "_HUMAN" at the end of each line
				line = line+'_HUMAN'
#if the line does not contain a pipe, i.e. the line doesnt contain a hofstenia contig id, then skip
			else:
				continue
#write each of the lines into the output files with a line break character at the end.
#this ensures that each gene name will be in the same row
			output_file.write(line+'\n')

#for each file that is processed, print out test telling the user what file the converted contents
#were written to
	string = 'Successfully converted {} to GO{}.txt'
	final_string = string.format(files,files)
	print(final_string)
