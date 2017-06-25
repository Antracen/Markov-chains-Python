import sys
import random
import re

# Read input, find all words and punctuation.
text = sys.stdin.read()
words = re.findall(r"[\w']+|[.,!?;:]", text)

# Dictionary detailing which words follow which starting words.
# Example: following["To"] = [be, eat, sleep]
# Can contain duplicates to keep track of popular following words.
following = {}

# Update following dictionary.
for i in range(len(words)):
	if i+1 < len(words):
		if not words[i] in following:
			following[words[i]] = []
		following[words[i]].append(words[i+1])

# Find a capital letter to start the sentence.
capital_words = list(filter(lambda word: word[0].isupper(), list(following)))
start_word = "Alice" #random.choice(capital_words)
ret = [start_word]

# Create sentence until we come to a full stop.
while True:
	following_word = random.choice(following[start_word])
	ret.append(following_word)
	if re.match("[.!?]", following_word):
		break
	start_word = following_word

for word in ret:
	if re.match("[.,!?;]", word):
		print("" + word, end="")
	else:
		print(" " + word, end="")
