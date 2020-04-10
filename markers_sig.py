#!/usr/bin/env python3

import sys

for files in sys.argv[1:]:
	with open(files, "r") as inputfile, open("positive_sig"+files,"w") as outputfile:
		n = 0
		for line in inputfile:
			n += 1
			line = line.rstrip()
			line_list = line.split("\t")
			if n ==1:
				continue
			if float(line_list[2]) > 0 and float(line_list[5]) < 0.05:
				outputfile.write(line+'\n')




