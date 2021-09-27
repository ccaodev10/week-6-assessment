from math import trunc
import random
d = {}
with open("WheelWords.txt") as f:
    for line in f:
        (key, val) = line.split()
        d[key] = val       
print ("Welcome to Wheel of Fortune!")
Round = 1
Player1Money = 0
Player2Money = 0
Player3Money = 0
while Round < 3:
    RoundOver = False
    enable1Vowel = False
    enable2Vowel = False
    enable3Vowel = False
    word, category = random.choice(list(d.items()))
    word = word.upper()
    word_completion = "_" * len(word)
    while RoundOver is False:
        Player1Turn = True
        Player2Turn = True
        Player3Turn = True
        while Player1Turn is True:
            print("The category is:",category)
            print(word_completion)
            print("It is your turn player 1. You have $"+str(Player1Money))
            choice = input("What will you do? [1] to guess the word [2] to guess a letter: ")
            if choice == '1':
                guess_word = input("Guess the word: ").upper()
                if guess_word == word:
                    print("That's correct! You win the round")
                    Round += 1
                    RoundOver = True
                    Player2Turn = False
                    Player3Turn = False
                    break
                else: 
                    print("That is incorrect")
                    Player1Turn = False
            elif choice == '2':
                spin = random.choice(open("WheelNumbers.txt").read().split())
                if spin == 'BANKRUPT':
                    print("You went bankrupt.")
                    Player1Money = 0
                    break
                elif spin == "LOSETURN":
                    print("You lost your turn.")
                    Player1Turn = False
                else:
                    print("You spun $"+spin)
                    guess = input("Guess a letter: ").upper()
                    if guess in ['A','E','I','O','U']:
                        if enable1Vowel is True:
                            Player1Money = Player1Money - 250
                            spin = 0
                        else:
                            print("You need to correctly guess a consonant before buying a vowel.")
                            continue
                    if guess in word_completion:
                        print("That letter is already in the word.")
                        Player1Turn = False
                    elif guess in word:
                        word_as_list = list(word_completion)
                        indices = [i for i, letter in enumerate(word) if letter == guess]
                        for index in indices:
                            word_as_list[index] = guess
                        word_completion = "".join(word_as_list)
                        Player1Money = Player1Money + int(spin)
                        enable1Vowel = True
                    else: 
                        print("That letter is not in the word.")
                        Player1Turn = False
            else: print("Not a valid choice.")
        while Player2Turn is True:
            print("The category is:",category)
            print(word_completion)
            print("It is your turn player 2. You have $"+str(Player2Money))
            choice = input("What will you do? [1] to guess the word [2] to guess a letter: ")
            if choice == '1':
                guess_word = input("Guess the word: ").upper()
                if guess_word == word:
                    print("That's correct! You win the round")
                    Round += 1
                    RoundOver = True
                    Player3Turn = False
                    break
                else: 
                    print("That is incorrect")
                    Player2Turn = False
            elif choice == '2':
                spin = random.choice(open("WheelNumbers.txt").read().split())
                if spin == 'BANKRUPT':
                    print ("You went bankrupt.")
                    Player2Money = 0
                    break
                elif spin == "LOSETURN":
                    print("You lost your turn.")
                    Player2Turn = False
                    break
                else:
                    print("You spun $"+spin)
                    guess = input("Guess a letter: ").upper()
                    if guess in ['A','E','I','O','U']:
                        if enable2Vowel is True:
                            Player2Money = Player2Money - 250
                            spin = 0
                        else:
                            print("You need to correctly guess a consonant before buying a vowel.")
                            continue
                    if guess in word_completion:
                        print("That letter is already in the word.")
                        Player2Turn = False
                    elif guess in word:
                        word_as_list = list(word_completion)
                        indices = [i for i, letter in enumerate(word) if letter == guess]
                        for index in indices:
                            word_as_list[index] = guess
                        word_completion = "".join(word_as_list)
                        Player2Money = Player2Money + int(spin)
                        enable2Vowel = True
                    else: 
                        print("That letter is not in the word.")
                        Player2Turn = False
            else: print("Not a valid choice.")
        while Player3Turn is True:
            print("The category is:",category)
            print(word_completion)
            print("It is your turn player 3. You have $"+str(Player3Money))
            choice = input("What will you do? [1] to guess the word [2] to guess a letter: ")
            if choice == '1':
                guess_word = input("Guess the word: ").upper()
                if guess_word == word:
                    print("That's correct! You win the round")
                    Round += 1
                    RoundOver = True
                    break
                else: 
                    print("That is incorrect")
                    Player3Turn = False
            elif choice == '2':
                spin = random.choice(open("WheelNumbers.txt").read().split())
                if spin == 'BANKRUPT':
                    print("You went bankrupt.")
                    Player3Money = 0
                    break
                elif spin == "LOSETURN":
                    print("You lost your turn")
                    Player3Turn = False
                    break
                else:
                    print("You spun $"+spin)
                    guess = input("Guess a letter: ").upper()
                    if guess in ['A','E','I','O','U']:
                        if enable3Vowel is True:
                            Player3Money = Player3Money - 250
                            spin = 0
                        else:
                            print("You need to correctly guess a consonant before buying a vowel.")
                            continue
                    if guess in word_completion:
                        print("That letter is already in the word.")
                        Player3Turn = False
                    elif guess in word:
                        word_as_list = list(word_completion)
                        indices = [i for i, letter in enumerate(word) if letter == guess]
                        for index in indices:
                            word_as_list[index] = guess
                        word_completion = "".join(word_as_list)
                        Player3Money = Player3Money + int(spin)
                        enable3Vowel = True
                    else: 
                        print("That letter is not in the word.")
                        Player3Turn = False
            else: print("Not a valid choice.")
finalMoney = 0
if Player1Money >= Player2Money and Player1Money >= Player3Money:
    print("Player1 is playing the final round.")
    finalMoney = Player1Money
elif Player2Money >= Player1Money and Player2Money >= Player3Money:
    print("Player2 is playing the final round.")
    finalMoney = Player2Money
else:
    print("Player3 is playing the final round.")
    finalMoney = Player3Money
word, category = random.choice(list(d.items()))
word = word.upper()
word_completion = "_" * len(word)
for guess in ['R','S','T','L','N','E']:
    word_as_list = list(word_completion)
    indices = [i for i, letter in enumerate(word) if letter == guess]
    for index in indices:
        word_as_list[index] = guess
    word_completion = "".join(word_as_list)
print('The category is:',category)
print(word_completion)
finalCorrect = False
while finalCorrect is False:
    finalAsk = input("Choose 3 consonants and 1 vowel: ").upper()
    finalAsk = list(finalAsk)
    if len(finalAsk) != 4:
        print("Please enter only four characters.")
    else:
        consonants = 0
        vowels = 0
        for i in finalAsk:
            if i.isalpha() == 0:
                print(i,"is not a letter")
                continue
            if i in ['A','E','I','O','U']:
                vowels += 1
            else:
                consonants += 1
        if consonants == 3 and vowels == 1:
            for guess in finalAsk:
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
            print(word_completion)
            finalGuess = input("Please guess the word: ").upper()
            if finalGuess == word:
                finalMoney += 10000
                print("Congrats! You won",finalMoney)
                break
            else:
                print("That is incorrect. The correct word is",word,"and you get",finalMoney)
                break
        else:
            print("Incorrect letters. You gave us",consonants,"consonants and",vowels,"vowels.")