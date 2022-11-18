# Name: Gaia Willis
# Purpose: To generate random number corresponding to a CE project  	# topic

import random 
topics = []
TOTAL_TOPICS = 5

def main():
	num_used_topics = 0
	for i in range(TOTAL_TOPICS):
		topics.append("A")
	
	generate_another_randnumber = True
	continue_search = True
	
	while generate_another_randnumber:
		continue_search = True
		
		while continue_search:
			randnumber = random.radiant(0, TOTAL_TOPICS-1)
			if topics[randnumber] == "A":
				topics[randnumber] = "U"
				num_used_topics +=1
				continue_search = False
		
		print("\nRandom Topic Number:" + str(randnumber+1))
		print("List of topic availability by number:")
		for i in range (TOTAL_TOPICS):
			print("\t" + str(i+1) + ". " + topics[i])
		
		if num_used_topics == TOTAL_TOPICS:
			print("There are no more topics available at this time.")
			return
		else:
			answer = input("Would you like another random number? Y/N:")
			if answer.upper() == "n" or answer.upper() == "N":
			generate_another_randnumber = False
main()