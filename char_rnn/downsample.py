import sys
import random

infile = sys.argv[1]
outfile = sys.argv[2]
percent_to_keep = float(sys.arg[3])

with open(infile, 'r') as big, open(outfile, 'w') as out:
	for example in big:
		if (random.randint(100) < percent_to_keep):
			out.write(example)
