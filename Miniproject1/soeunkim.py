from pattern.web import *
w = Wikipedia()

olympic_medalists_in_figure_skating = URL('https://en.wikipedia.org/wiki/List_of_Olympic_medalists_in_figure_skating').download()
all_text = plaintext(olympic_medalists_in_figure_skating)
edit = all_text.split('[edit]')


### men's medalists ###

# It would be easier to read your code if you left a comment
# explaining why you're selecting certain lines and deleting others
men_medalists = edit[2]
men_medalists_lines = men_medalists.split('\n')
del men_medalists_lines[:13]
del men_medalists_lines[2]
del men_medalists_lines[48:]

men_gold = []
men_silver = []
men_bronze = []
olympic_year_name = []

for i in range(len(men_medalists_lines)):
	# Again, a comment here would be good! What is men_medalists_lines
	# and why are you parsing it this way?
	if i%2==0:
		olympic_year_name.append(men_medalists_lines[i])
	else:
		word_men = men_medalists_lines[i].split('  ')
		del word_men[0]
		for j in range(len(word_men)):
			man_name = word_men[j].split(' ')
			# vv You could also use del man_name[-1] -- same thing
			del man_name[len(man_name)-1]

			# This is handling multi-word last names, yes? Would be good to
			# leave a comment so it's clear why you're doing these things
			man_name_1 = man_name[0]
			del man_name[0]
			for k in range(len(man_name)):
				man_name_1 = man_name_1 + '_' + man_name[k]
			if j==0:
				men_gold.append(man_name_1)
			elif j==1:
				men_silver.append(man_name_1)
			else:
				men_bronze.append(man_name_1)


### gold ###

man_gold_birth = []
for i in range(len(men_gold)):
	man_gold_url = URL('https://en.wikipedia.org/wiki/'+men_gold[i]).download()
	man_gold_text = plaintext(man_gold_url)
	if man_gold_text.find('Born')==-1:
		# So if the wikipedia page doesn't contain the word "Born", you search for a different URL?
		# Why? Leave a comment so the next reader knows!
		man_gold_url = URL('https://en.wikipedia.org/wiki/'+men_gold[i]+'_(figure_skater)').download()
		man_gold_text = plaintext(man_gold_url)
	else:
		pass

	man_gold_text_list = man_gold_text.split('\n')
	for j in range(len(man_gold_text_list)):
		if man_gold_text_list[j]=='Born':
			man_gold_birth.append(man_gold_text_list[j+1])
		else:
			pass


olympic_year = []
for i in range(len(olympic_year_name)):
	yearnamelist = olympic_year_name[i].split(' ')
	olympic_year.append(yearnamelist[0])

# ^^ You could also do:
# for olympic_details in olympic_year_name:
# 	yearnamelist = olympic_details.split(' ')
# 	olympic_year.append(yearnamelist[0])


man_gold_age = []
for i in range(len(man_gold_birth)):
	man_gold_age_list = man_gold_birth[i].split('-')
	age = man_gold_age_list[0]
	age = age[1:]
	man_gold_age.append(age)

# ^^ Same here -- you don't need to use i and range

age_got_gold_medal=[]
for i in range(len(man_gold_age)):
	subtract =int(olympic_year[i]) - int(man_gold_age[i])
	age_got_gold_medal.append(subtract)

# ^^ This is a good use of for i in range -- you need to use i
# in two lists, not just in the list you're looping through


### calculation ###

average_gold_age = sum(age_got_gold_medal)/len(age_got_gold_medal)

# For youngest_gold_age and oldest_gold_age, check out list.index(item)
# https://docs.python.org/2/tutorial/datastructures.html
youngest_gold_age = min(age_got_gold_medal)
for i in range(len(men_gold)):
	if age_got_gold_medal[i] == min(age_got_gold_medal):
		youngest_gold_name = men_gold[i]

oldest_gold_age = max(age_got_gold_medal)
for i in range(len(men_gold)):
	if age_got_gold_medal[i] == max(age_got_gold_medal):
		oldest_gold_name = men_gold[i]

def men_gold_age_graph():
	for i in range(len(age_got_gold_medal)):
		# Also a good use of for i in range
		print olympic_year[i] + ' ' + '*'*int(age_got_gold_medal[i])
	print '    5    10   15   20   25   30'


while True:
	# I like the way you handled user input!
	answer = raw_input('What do you want to know in men gold medalists?\naverage age / youngest medalist / oldest medalist / age graph / end\n')
	if answer == 'average age':
		print average_gold_age
	elif answer == 'youngest medalist':
		print youngest_gold_name + ', ' + str(youngest_gold_age)
	elif answer == 'oldest medalist':
		print oldest_gold_name + ', ' + str(oldest_gold_age)
	elif answer == 'age graph':
		men_gold_age_graph()
	elif answer == 'end':
		print 'Thank you'
		break



