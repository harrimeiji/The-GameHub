# HarriDesigns
from random import randint
import time
import pickle

mainMenuprint = ('{:>20}'.format('''
====================================
            MAIN MENU
1. Play Memory Game
2. Play Memory Game (Speed)
===================================='''))

numbers = []

class MemoryGame:

    def __init__(self):
        pass

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
        while runTime < 1:
            if memoryMenuChoice == 1:
                memoryStart = MemoryGame()
                memoryStart.memory()
                runTime += 1
            if memoryMenuChoice == 2:
                memoryStart = MemoryGame()
                memoryStart.memoryLeaderboard()
                runTime += 1


    def endMethod(self):
        print('{:^120}'.format('Game Over!'))
        exit()


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
            with open('memoryGameLeaderboards.pkl', 'ab') as memorylbSave:
                pickle.dump(memorylbHiveMind, memorylbSave)

    def memory(self):
        yourGuess = []
        while True:
            if yourGuess == numbers:
                yourGuess = []
                numbers.append(randint(1, 9))
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
                        memoryClass.saveMethod()
                        memoryClass.endMethod()
                    else:
                        yourGuess.append(temp)
                        time_after = time.time()
                        if time_after - time_passed > 5:
                            MemoryClass = MemoryGame()
                            MemoryClass.saveMethod()
                            MemoryClass.endMethod()

            else:
                MemoryClass = MemoryGame()
                MemoryClass.saveMethod()
                MemoryClass.endMethod()

    def memoryLeaderboard(self):
        print('\n')
        e = []
        with open('memoryGameLeaderboards.pkl', 'rb') as memorylbSave:
            e.append(pickle.load(memorylbSave))
        memorySortedList = sorted(e, key=lambda d: d['Score'], reverse=True)
        for i in memorySortedList:
            tempList = i
            for k, v in tempList.items():
                print(str(k) + ' : ' + str(v))


class SpeedMemory(MemoryGame):

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
            with open('speedGameLeaderboards.pkl', 'ab') as memorylbSave:
                pickle.dump(memorylbHiveMind, memorylbSave)


    def speedMemory(self):
        yourGuess = []
        counter = 0
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

        roundsLeft = 5
        print('You have ' + str(roundsLeft - counter) + ' until the game gets faster.')
        counter += 1
        while True:
            if yourGuess == numbers:
                yourGuess = []
                numbers.append(randint(1, 9))
                print('Memorize: ')
                for i in numbers:
                    print(i)
                time.sleep(2)
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

    def speedMemoryLeaderboard(self):
        print('\n')
        e = []
        with open('speedGameLeaderboards.pkl', 'rb') as memorylbSave:
            while True:
                try:
                    e.append(pickle.load(memorylbSave))
                except EOFError:
                    break
        memorySortedList = sorted(e, key=lambda d: d['Score'], reverse=True)
        for i in memorySortedList:
            tempList = i
            for k, v in tempList.items():
                print(str(k) + ' : ' + str(v))


a = MemoryGame()
b = SpeedMemory()
print(mainMenuprint)
mainMenu = input('Select your option: ')

if mainMenu == '1':
    a.mainMenuprint()
elif mainMenu == '2':
    b.mainMenuprint()