import os
import copy
import random

path = "D:\\GameShortcuts"

def getRandGame():
    onlyfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    shortcuts = copy.deepcopy(onlyfiles)
    for f in range(0, len(onlyfiles)):
        onlyfiles[f] = onlyfiles[f].split('.')[0]
    rand = random.randint(0, len(onlyfiles))
    print('\n')
    print(onlyfiles[rand])
    return shortcuts[rand]


while True:
    randGameShortcut = getRandGame()
    print('Press [Y] and [Enter] to play')
    print('Press [N] and [Enter] to re-roll')
    print('\n\nPress [Enter] to exit this window')
    response = input('\n')
    if ('y' in response) or ('Y' in response):
        os.startfile(path + "\\" + randGameShortcut)
        break
    elif ('n' in response) or ('N' in response):
        #print("\r")
        #print("--------------------------------\n")
        os.system('cls') #windows only
        continue
    else:
        break
