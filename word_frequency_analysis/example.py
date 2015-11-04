""" Analyzes the word frequencies in a book downloaded from
    Project Gutenberg """

import string

file_name = "pg32325.txt"

#print lines

punctuation = string.punctuation
whitespace = ['\t','\n','\x0b','\x0c','\r',' ']



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

    lines = lines[first_line:first_line+50]



    for i in range(len(punctuation)/2):
        for j in range(len(lines)):
            lineslist1 = []
            a = lines[j].replace(punctuation[i*2],'')
            lineslist1.append(a)
        for k in range(len(lineslist1)):
            lines = []
            a = lineslist1[k].replace(punctuation[i*2+1])
            lines.append(a)




    for i in range(len(lines)):
        a = lines[i].split(punctuation[0])
        lineslist1.append(a)
    for i in range(len(lineslist1)):
        a = lineslist1[i].split(punctuation[1])
        lineslist2.append(a)



    for i in range(len(punctuation)-2):
        for j in range(len(lineslist2)):
            lineslist1=[]
            a = lineslist2[j].split(punctuation[i+2])
            lineslist1.append[a]
        for k in range(len(lineslist1)):
            lineslist2 = []
            a = lineslist1[k].split(punctuation[i+3])
            lineslist2.append(a)

    print lineslist2


get_word_list(file_name)

def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
        occurring words ordered from most to least frequently occurring.

        word_list: a list of words (assumed to all be in lower case with no
                    punctuation
        n: the number of words to return
        returns: a list of n most frequently occurring words ordered from most
                 frequently to least frequentlyoccurring
    """
    pass


