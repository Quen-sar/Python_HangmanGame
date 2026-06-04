import random
import sys
#pyinstaller --onefile HangmanGame_V2.py
#########################################################################################################
#check for null input
def checkNull(guess):
    if not guess:
        sys.exit("\nNull detected, ending session\n")
    else:
        return guess
#########################################################################################################
def displayMeth(blank):
    blankArr = []
    for i in blank:
        blankArr.append(i)
    print(" ".join(str(x) for x in blankArr), "\n")
#########################################################################################################
def showMan(tries):
    head = "    -----    \n   | o,o |   \n   | ___ |   \n    -----    "
    neck = "      |      \n      |      "
    arms = "------|------"
    back = "      |      \n      |      \n      |      \n      |      \n      |      \n      |      "
    legs = "     / \     \n    /   \    \n   /     \   \n  /       \  \n /         \ "

    if tries == 9:
        head = "    -----    \n   | o,o |   \n   |     |   \n    -----    "
    elif tries == 8:
        head = "    -----    \n   | o o |   \n   |     |   \n    -----    "
    elif tries == 7:
        head = "    -----    \n   |   o |   \n   |     |   \n    -----    "
    elif tries == 6:
        head = "    -----    \n   |     |   \n   |     |   \n    -----    "
    elif tries == 5:
        head = "    -----    \n   |     |   \n   |     |   \n    -----    "
        legs = "       \     \n        \    \n         \   \n          \  \n           \ "
    elif tries == 4:
        head = "    -----    \n   |     |   \n   |     |   \n    -----    "
        legs = "             \n             \n             \n             \n             "
    elif tries == 3:
        head = "    -----    \n   |     |   \n   |     |   \n    -----    "
        legs = "             \n             \n             \n             \n             "
        arms = "      |------"
    elif tries == 2:
        head = "    -----    \n   |     |   \n   |     |   \n    -----    "
        legs = "             \n             \n             \n             \n             "
        arms = "      |      "
    elif tries == 1:
        head = "    -----    \n   |     |   \n   |     |   \n    -----    "
        neck = "             \n             "
        legs = "             \n             \n             \n             \n             "
        arms = "             "
        back = "             \n             \n             \n             \n             \n             "
    elif tries == 0:
        head = ""
        neck = ""
        arms = ""
        back = ""
        legs = ""

    print(head)
    print(neck)
    print(arms)
    print(back)
    print(legs)
    print(" ")
#########################################################################################################
def guessMeth(blank, word, tries):
    guess = input("Guess a letter: ")
    checkNull(guess)
    if guess in word:    
        print("correct guess\n")
        blank = "".join([guess if word[i] == guess else blank[i] for i in range(len(word))])
    else:
        print("incorrect guess\n")

    showMan(tries)
    displayMeth(blank)
    return blank
#########################################################################################################
#main method
wordArr =  ["apple", "banana", "orange", "grape", "school", "animal", "window", "garden", "laptop",
            "planet", "pencil", "castle", "bridge", "dollar", "jungle", "travel", "monkey", "butter",
            "flower", "friend", "guitar", "puzzle", "rocket", "bottle", "dragon", "candle", "cheese",
            "doctor", "summer", "winter", "autumn", "spring", "cloud", "desert", "forest", "pirate",
            "ticket", "zebra", "yellow", "purple", "number", "sugar", "cookie", "silver", "golden",
            "letter", "shadow", "singer", "market", "parent", "rabbit"]

word = random.choice(wordArr)
blank = ("").rjust(len(word),"_") 
displayMeth(blank)

tries = 10
while tries >= 0:
    if blank == word:
        break
    blank = guessMeth(blank, word, tries)
    print("Guesses remaining: ", tries)
    tries -= 1
print("===================================================================")
if blank == word:
    print("\nWell done, you won\n")
else:
    print("\nNo tries left, game over\n")
print("===================================================================")
input()
#########################################################################################################