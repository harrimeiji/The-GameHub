# HarriDesigns
from random import randint
import time
import pickle

mainMenuprint = ('{:>20}'.format('''
====================================
            MAIN MENU
1. Play Memory Game
2. Show Leaderboards

===================================='''))

numbers = []

class MemoryGame:

    def __init__(self):
        pass



    def endMethod(self):
        print('{:^120}'.format('Game Over!'))
        exit()


    def saveMethod(self):
        score = -1
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
print(mainMenuprint)
mainMenu = input('Select your option: ')

if mainMenu == '1':
    a.memory()
elif mainMenu == '2':
    a.memoryLeaderboard()
