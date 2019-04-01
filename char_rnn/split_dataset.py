import csv
import sys
import random

test_percent = 10
valid_percent = 10

train_file = 'data/train.txt'
valid_file = 'data/valid.txt'
test_file = 'data/test.txt'

with open(train_file, 'w') as train, open(valid_file, 'w') as valid, open(test_file, 'w') as test:
	for filename in sys.argv[1:]:
		with open(filename, 'r') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				# only keep the tweets not the metadata
				tweet = row['tweet'] + '\n'
				rand = random.randint(0, 100)
				if (rand < test_percent):
					test.write(tweet)
				elif (rand < test_percent + valid_percent):
					valid.write(tweet)
				else:
					train.write(tweet)
