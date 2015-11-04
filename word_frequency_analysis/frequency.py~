""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string


punctuation = string.punctuation



def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""

	f = open(file_name,'r')
	lines = f.readlines()
	first_line = 0
	last_line = 0

	while lines[first_line].find('CONTENT') == -1:
		first_line += 1
	while lines[last_line].find('THE END') == -1:
		last_line += 1

	lines = lines[first_line:first_line+200]
	wordslist = []
	lineslist1 = []
	finallist = []



	for i in range(len(lines)):
		lineslist = lines[i].split()
		for j in range(len(lineslist)):
			wordslist.append(lineslist[j])



	for i in range(len(punctuation)/2):
		for j in range(len(wordslist)):
			a = wordslist[j].replace(punctuation[i*2],'')
			lineslist1.append(a)
		wordslist = []
		for k in range(len(lineslist1)):
			a = lineslist1[k].replace(punctuation[i*2+1],'')
			wordslist.append(a)
		lineslist1 = []


	for i in range(len(wordslist)):
		a = wordslist[i].lower()
		finallist.append(a)

	return finallist




def get_top_n_words(word_list,n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	word_counts = dict()
	for c in word_list:
		if c not in word_counts:
			word_counts[c] = 1
		else:
			word_counts[c] += 1
	
	ordered_by_frequency = sorted(word_counts, key=word_counts.get, reverse=True)
	
	
	for i in range(n):
		print ordered_by_frequency[i]

