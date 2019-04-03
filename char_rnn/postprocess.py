"""
Post-processing script removing excess white space and <eos> tags,
and inserting new lines between tweets.
"""

import sys

with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'w') as out:
	for tweet in f.read().split('<eos>'):
		tweet_char = list(tweet)
		if (tweet_char[0] is ' '):
			out.write(''.join(list(tweet)[1::2]) + '\n')
		else:
			out.write(''.join(list(tweet)[::2]) + '\n')
