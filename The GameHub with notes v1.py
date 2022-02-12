# HarriDesigns
# Importing necessary modules.

# Contents Library:
# MemoryGame: Lines 21 -

from random import randint
import time
import pickle
# Using {:>20} and .format() to print the menu near the middle of the page.
mainMenuprint = ('{:>20}'.format('''
====================================
            MAIN MENU
1. Play Memory Game
2. Show Leaderboards

===================================='''))
# Creating a Global Variable for most classes/functions to use.
numbers = []


class MemoryGame:   # Thia is the Memory Game.

    def __init__(self):
        pass


# this is the main menu to print the memory inside
    def mainMenuprint(self):
        print('{:>20}'.format('''
====================================
        MEMORY GAME MAIN MENU
1. Play Memory Game
2. Show Leaderboards

===================================='''))

# This will we used later to print game over and to end the code.
    def endMethod(self):
        print('{:^120}'.format('Game Over!'))
        exit()

# this is my save mechanism.
    def saveMethod(self):
        score = -1    # numbers list will be 1 higher than yourGuess which is defined later.
        print('You lost.')
        x = input('do you want to save?: ')
        if x == 'yes':
            y = input('what is your name?: ')
            for i in numbers:
                score += 1
            memorylbHiveMind = {'Name': y, 'Score': score}
            with open('memoryGameLeaderboards.pkl', 'ab') as memorylbSave:   # simple save file method.
                pickle.dump(memorylbHiveMind, memorylbSave)

# this is the memory game.
    def memory(self):
        yourGuess = []
        while True:   # this is a mostly indefinite loop, only ending when someone loses.
            if yourGuess == numbers:
                yourGuess = []   # clearing the yourGuess variable as we input all numbers again.
                numbers.append(randint(1, 9))   # giving numbers, a random integer between 1 and 9.
                print('Memorize: ')
                for i in numbers:
                    print(i)   # printing all numbers with a for loop.
                time.sleep(5)   # waiting 5 seconds for people to read the numbers.
                for i in range(500):   # simplest way to make sure people cannot go back up to check the numbers.
                    print('\n')
                for i in range(len(numbers)):   # this is going to repeat the code below for each turn passed.
                    time_passed = time.time()   # this is a time variable to get the current time, it is used later.
                    temp = input('enter 1 of the numbers in the order you saw them: ')
                    temp = int(temp)   # turning the guess into an input.
                    if temp > 9:
                        memoryClass = MemoryGame()   # Turning the class into a usable variable.
                        memoryClass.saveMethod()    # This is my saving mechanism.
                        memoryClass.endMethod()     # This is my game over mechanism.
                    else:
                        yourGuess.append(temp)   # Adding your input to the yourGuess list.
                        time_after = time.time()    # This is getting the time after the input.

                        # The reason to subtract the 2 time variables, is as the actual number is the difference
                        # from the 1st of Jan 1970 and now. So the difference between the 2 variables is time passed.
                        if time_after - time_passed > 5:
                            MemoryClass = MemoryGame()
                            MemoryClass.saveMethod()
                            MemoryClass.endMethod()

            else:
                MemoryClass = MemoryGame()
                MemoryClass.saveMethod()
                MemoryClass.endMethod()

# this is the leaderboards system.
    def memoryLeaderboard(self):
        print('\n')   # \n prints an empty line.
        e = []   # temporary list
        with open('memoryGameLeaderboards.pkl', 'rb') as memorylbSave:   # accessing the save file.
            while True:   # while True is an infinite loop unless broken with the break command.
                try:   # try means that the code will do something, until an error occurs, but it won't stop the code.
                    e.append(pickle.load(memorylbSave))   # adding the contents of the save file to e (the list)
                except EOFError:   # EOFError is when there is nothing left in a file, if one occurs, it does an action.
                    break   # this ends the while loop.
        memorySortedList = sorted(e, key=lambda d: d['Score'], reverse=True)
        for i in memorySortedList:
            tempList = i
            for k, v in tempList.items():
                print(str(k) + ' : ' + str(v))
        # sorted, sorts a list. it takes a list and a key, we want to sort by a specific key, so we can use the lambda
        # function, we use d as a key, however as we only want to sort them by the score value, we will make the key
        # d, but specifically for score, as specified with [], we then use reverse = true as naturally, sorted
        # is in descending order. we then iterate through the list to get the dictionaries with a for loop, then
        # we iterate through each dictionary getting the key and values and printing them.


a = MemoryGame()   # assigning MemoryGame to a variable to use
print(a.mainMenuprint())   # printing the menu with the menu function inside MemoryGame
mainMenu = input('Select your option: ')   # getting an option.

# using if an elif to run the correct function.
if mainMenu == '1':
    a.memory()
elif mainMenu == '2':
    a.memoryLeaderboard()
