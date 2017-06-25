# Markov-chains-Python

This Markov chain experiment generates random strings by analyzing an input file.

The program generates a text by starting on a randomly chosen word. The following word is determined by seeing which words followed the given word in our input file.

The more often a word Y follows a word X the more likely it is for the program to choose the word Y following X when generating the string.

Example:

	input: "hello this is cool is very nice yes it is cool"

	If the program has to choose a word to follow "is" with it will pick "cool" with a 2/3 probability and "very" with 1/3 probability.
