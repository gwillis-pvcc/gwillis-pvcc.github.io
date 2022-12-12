# Gaia Willis
import random

def main():
    global wordList
    playAgain = True
    
    while playAgain:
        printHeadings()
        printMenu()
        
        wordList = [] #clears the list from the last play
        wordFile = open(inFile, "r") #open the file for READ
        for textLine in wordFile: #read in a line of text from the file
            for word in textLine.split(): #split the line of text into two words
                wordList.append(word) #add each word to the word list
        wordFile.close()

        playGame()            
        yesno = input("Would you like to play again? (Y/N) ")
        if yesno == "n" or yesno == "N":
            playAgain = False
            print("Thank you for playing PORDLE!")
            return()

def printHeadings():
    print("\nWelcome to PORDLE! The PVCC Wordle Game.")
    print("I will think of a word and you try to guess the letters in the word.")
    print("The number of dashes indicates the number of letters in the word.")

def printMenu():
    global inFile
    print("\nChoose a PORDLE category:")
    print("\t1. Animals")
    print("\t2. Bio 102 Terms ")
    print("\t3. Greek Pantheon")
    print("\t4. Games")

    category = input("Please enter the category number: ")
    
    if category == "1":
        inFile = 'animals.txt'
        print("\nThis will be an ANIMAL Pordle")
    elif category == "2":
        inFile = 'plantanatomy.txt'
        print("\nThis will be a Plant anatomy Pordle (No spaces)")
    elif category == "3":
        inFile = 'provincia.txt'
        print("\nThis will be a Roman Province Pordle (No spaces)")
    elif category == "4":
        inFile = 'games.txt'
        print("\nThis will be a Game title Pordle (No spaces)")
    else:
            inFile = 'animals.txt'
            print("\nThis will be an ANIMAL Pordle")


def playGame():
    numGuesses = 1
    lettersUsed = []
        
    wordChosen = random.choice(wordList)
    pordle = wordChosen
    
    for i in range(len(pordle)):
        pordle = pordle[0:i] + "_" + pordle[i+1:] 
    print(" ".join(pordle)) 

    while pordle != wordChosen: 
        letterGuess = input("Please enter a letter: ")
        letterGuess = letterGuess.lower()
        lettersUsed.append(letterGuess) 
        print("Number of Guesses: " + str(numGuesses))

        for i in range(len(wordChosen)): 
            if wordChosen[i] == letterGuess:
                pordle = pordle[0:i] + letterGuess + pordle[i+1:]

        print("Used letters: ")
        print(lettersUsed)
        print(" ".join(pordle))
        numGuesses += 1

    print("Well done! You guessed in " + str(numGuesses-1) + " guesses!")

main()
