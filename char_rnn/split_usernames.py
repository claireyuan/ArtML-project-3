import sys
import random

test_percent = 10
valid_percent = 10

train_file = 'data/train.txt'
valid_file = 'data/valid.txt'
test_file = 'data/test.txt'

with open(train_file, 'w') as train, open(valid_file, 'w') as valid, open(test_file, 'w') as test:
	for filename in sys.argv[1:]:
		with open(filename, 'r') as reader:
			for row in reader:
				row = row + '\n'
				rand = random.randint(0, 100)
				if (rand < test_percent):
					test.write(row)
				elif (rand < test_percent + valid_percent):
					valid.write(row)
				else:
					train.write(row)
