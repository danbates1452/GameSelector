import os
import copy
from random import randint, shuffle

path = "D:\\GameShortcuts" #shortcut directory
# Constants
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
shuffle(files)
shortcuts = copy.deepcopy(files)


# Variables
unseen = copy.deepcopy(shortcuts)
attempt_count = 0

def remove_file_extension(filename):
    return filename.rsplit('.', 1)[0]

def get_random_game():
    global shortcuts, unseen, attempt_count
    if (len(unseen)) == 0:
        unseen = copy.deepcopy(shortcuts)
        attempt_count = 0

    rand = randint(0, len(unseen) - 1)

    attempt_count += 1
    how_many_seen = ''.join(['(', str(attempt_count),'/', str(len(shortcuts)), ')'])
    print('\n')
    print(remove_file_extension(unseen[rand]), how_many_seen)

    return unseen.pop(rand)

while True:
    randGameShortcut = get_random_game()
    print('Press [Y] and [Enter] to play')
    print('Press [N] and [Enter] to re-roll')
    print('\n\nPress just [Enter] to exit this window')
    response = input('\n')
    if ('y' in response) or ('Y' in response):
        os.startfile(path + "\\" + randGameShortcut)
        break #break the loop (end the script here)
    elif ('n' in response) or ('N' in response):
        os.system('cls') #windows only - clear the console
        continue #continue looping
    else:
        break #break the loop (end the script here)
