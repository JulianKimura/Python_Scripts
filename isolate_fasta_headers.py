#!/usr/bin/env python3

#this script will take a fasta file, and print out a new text file containing all of the header information, without the '>' symbol

with open('8_26_19_hmi_transcriptome_20140211_filtered_long_annotated.fasta', 'r') as input_file, open('transcriptome_headers.txt', 'w') as output_file:
	for line in input_file:
		if '>' in line:
			line = line.rstrip()
			edited_line = line.replace('>', '')
			output_file.write(edited_line)



