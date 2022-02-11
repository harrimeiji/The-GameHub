# HarriDesigns
# importing modules
from random import randint
import time
import pickle

# formatting menu
mainMenuprint = ('{:>20}'.format('''   
====================================
            MAIN MENU
1. Play Memory Game
2. Play Memory Game (Speed)
===================================='''))
# creating global variable
numbers = []

# creating game 1's class
class MemoryGame:

    def __init__(self):
        pass

    # defining main menu
    def mainMenuprint(self):
        print('{:>20}'.format('''
====================================
        MEMORY GAME MAIN MENU
1. Play Memory Game
2. Show Leaderboards

===================================='''))
        print('\n')
        memoryMenuChoice = input('Select a number: ')
        memoryMenuChoice = int(memoryMenuChoice)
        runTime = 0

        # creating 1 successful time while loop
        while runTime < 1:
            if memoryMenuChoice == 1:
                # running functions inside the class
                memoryStart = MemoryGame()
                memoryStart.memory()
                runTime += 1
            if memoryMenuChoice == 2:
                memoryStart = MemoryGame()
                memoryStart.memoryLeaderboard()
                runTime += 1

    # defining ending function
    def endMethod(self):
        print('{:^120}'.format('Game Over!'))
        exit()

    # defining save function
    def saveMethod(self):
        score = -1
        time.sleep(3)
        print('You lost.')
        x = input('do you want to save?: ')
        if x == 'yes':
            y = input('what is your name?: ')
            for i in numbers:
                score += 1
            memorylbHiveMind = {'Name': y, 'Score': score}
            # saving binary to a file using pickling
            with open('memoryGameLeaderboards.pkl', 'ab') as memorylbSave:
                pickle.dump(memorylbHiveMind, memorylbSave)

    # defining the game function
    def memory(self):
        yourGuess = []
        while True:
            if yourGuess == numbers:
                yourGuess = []
                # adding random integers
                numbers.append(randint(1, 9))
                print('Memorize: ')
                for i in numbers:
                    print(i)
                time.sleep(5)
                # created an empty space
                for i in range(500):
                    print('\n')
                for i in range(len(numbers)):
                    time_passed = time.time()
                    temp = input('enter 1 of the numbers in the order you saw them: ')
                    temp = int(temp)
                    if temp > 9:
                        # ending game method
                        memoryClass = MemoryGame()
                        memoryClass.saveMethod()
                        memoryClass.endMethod()
                    else:
                        yourGuess.append(temp)
                        time_after = time.time()
                        # finding time passed
                        if time_after - time_passed > 5:
                            MemoryClass = MemoryGame()
                            MemoryClass.saveMethod()
                            MemoryClass.endMethod()

            else:
                MemoryClass = MemoryGame()
                MemoryClass.saveMethod()
                MemoryClass.endMethod()

    # defining leaderboard function
    def memoryLeaderboard(self):
        print('\n')
        e = []
        # opening file with pickling
        with open('memoryGameLeaderboards.pkl', 'rb') as memorylbSave:

            # emptying file contents to list
            while True:
                try:
                    e.append(pickle.load(memorylbSave))
                except EOFError:
                    break

        # sorting by the key/value score, where d is score in d.
        memorySortedList = sorted(e, key=lambda d: d['Score'], reverse=True)

        # iterating through the list/dict
        for i in memorySortedList:
            tempList = i
            for k, v in tempList.items():
                print(str(k) + ' : ' + str(v))

# new game class inheriting old game class
class SpeedMemory(MemoryGame):

    # new main menu, follows rules of previous one
    def mainMenuprint(self):
        print('{:>20}'.format('''
    ====================================
            SPEED MEMORY MAIN MENU
    1. Play Memory Game ( SPEED )
    2. Show Leaderboards

    ===================================='''))
        print('\n')
        runTime = 0
        while runTime < 1:
            memoryMenuChoice = input('Select a number: ')
            memoryMenuChoice = int(memoryMenuChoice)
            if memoryMenuChoice == 1:
                memoryStart = SpeedMemory()
                memoryStart.speedMemory()
                runTime += 1
            if memoryMenuChoice == 2:
                memoryStart = SpeedMemory()
                memoryStart.speedMemoryLeaderboard()
                runTime += 1

    # defining new save function
    def saveMethod(self):
        score = -1
        time.sleep(3)
        print('You lost.')
        x = input('do you want to save?: ')
        if x == 'yes':
            y = input('what is your name?: ')
            for i in numbers:
                score += 1
            memorylbHiveMind = {'Name': y, 'Score': score}

            # saving binary to different file through pickling
            with open('speedGameLeaderboards.pkl', 'ab') as memorylbSave:
                pickle.dump(memorylbHiveMind, memorylbSave)

    # defining the game
    def speedMemory(self):
        yourGuess = []
        counter = 0

        # gives 5 turns before speedup
        while counter < 5:
            if yourGuess == numbers:
                yourGuess = []
                numbers.append(randint(1, 9))
                counter += 1
                roundsLeft = 5
                print('You have ' + str(roundsLeft - counter) + ' rounds until the game gets faster.')
                print('Memorize: ')
                for i in numbers:
                    print(i)
                time.sleep(5)
                for i in range(500):
                    print('\n')
                for i in range(len(numbers)):
                    time_passed = time.time()
                    temp = input('enter 1 of the numbers in the order you saw them: ')
                    temp = int(temp)
                    if temp > 9:
                        memoryClass = MemoryGame()
                        speedClass = SpeedMemory()
                        speedClass.saveMethod()
                        memoryClass.endMethod()
                    else:
                        yourGuess.append(temp)
                        time_after = time.time()
                        if time_after - time_passed > 3:
                            MemoryClass = MemoryGame()
                            speedClass = SpeedMemory()
                            speedClass.saveMethod()
                            MemoryClass.endMethod()
            else:
                MemoryClass = MemoryGame()
                speedClass = SpeedMemory()
                speedClass.saveMethod()
                MemoryClass.endMethod()

        # prints the rounds left till speedup
        roundsLeft = 5
        print('You have ' + str(roundsLeft - counter) + ' until the game gets faster.')
        counter += 1

        # this is the fast mode
        while True:
            if yourGuess == numbers:
                yourGuess = []
                numbers.append(randint(1, 9))
                print('Memorize: ')
                for i in numbers:
                    print(i)
                # less time by 3 seconds
                time.sleep(2)
                for i in range(500):
                    print('\n')
                for i in range(len(numbers)):
                    time_passed = time.time()
                    temp = input('enter 1 of the numbers in the order you saw them: ')
                    temp = int(temp)
                    if temp > 9:
                        # using both parent and child class functions
                        memoryClass = MemoryGame()
                        speedClass = SpeedMemory()
                        speedClass.saveMethod()
                        memoryClass.endMethod()
                    else:
                        yourGuess.append(temp)
                        time_after = time.time()

                        # gives 3 seconds less to input numbers
                        if time_after - time_passed > 2:
                            MemoryClass = MemoryGame()
                            speedClass = SpeedMemory()
                            speedClass.saveMethod()
                            MemoryClass.endMethod()
            else:
                MemoryClass = MemoryGame()
                speedClass = SpeedMemory()
                speedClass.saveMethod()
                MemoryClass.endMethod()

    # defines new leaderboard function
    def speedMemoryLeaderboard(self):
        print('\n')
        e = []
        with open('speedGameLeaderboards.pkl', 'rb') as memorylbSave:

            # empties file to new list
            while True:
                try:
                    e.append(pickle.load(memorylbSave))
                except EOFError:
                    break
        # sorts by using d as score in d as key
        memorySortedList = sorted(e, key=lambda d: d['Score'], reverse=True)

        # iterates through lists
        for i in memorySortedList:
            tempList = i
            for k, v in tempList.items():
                print(str(k) + ' : ' + str(v))

# defining classes to variables and printing menu
a = MemoryGame()
b = SpeedMemory()
print(mainMenuprint)
mainMenu = input('Select your option: ')

# acts according to input
if mainMenu == '1':
    a.mainMenuprint()
elif mainMenu == '2':
    b.mainMenuprint()