# Name: Gaia Willis
#	Prog purpose: This Magic 8-ball code uses a python tuple since the 
#				use does not have the ability to change the 8-ball answers
				
import random
answers_8_ball=("As I see it, yes", "Ask again later", "Better not 	tell you now", "Cannot predict now", "Concentrate and ask again", 	"Don't count on it", "It is certain", "It is decidedly so", "Most 	likely", "My reply is no", "My sources say no", "Outlook good", 	"Outlook not so good", "Reply hazy try again", "Signs point to yes", 	"Very doubtful", "Without a doubt", "Yes definitely", "You may rely 	on 	it")
def main():
print("I am the MAGIC-8 ball and I can answer any yes or no question")
another_question=True
while another_question:
	answer=random.choice(answers_8_ball)
	print("\nShake the MAGIC_8_ball")
	print("...and now...")
	question=input("\nwhat is your YES or NO question")
	print("The MAGIC-8 ball says:"+answer)
	
	askAgain=input("\nWould you like to ask me another question (Y or N)?:")
	id askAgain.upper()=="N" or askAgain=="n":
	another_question=False 
print("\nCome back again when you have other important questions.")
print("...Magic-8 Ball OUT.")
main()