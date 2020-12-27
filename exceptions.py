'''a list of all required custom exceptions
which includes such exceptions as GameOver, EnemyDown
CommandException and WrongHeroExc'''

import datetime as dt

class GameOver(Exception): # when a user doesn't have hp

    def __str__(self): #repr for traceback
        return "The Game is over - u have no lives"

    #documenting results to a certain file
    def write_score(self, user):
        file = open('./scores.txt', 'r+')
        lines = file.readlines()
        all_scores = [list(line.split())[1] for line in lines]
        score_data = dt.datetime.now().strftime('%Y-%m-%d %H:%M')
        if len(all_scores) < 10:
            file.write(f'{user.name}: {user.score} ({score_data})\n')
            file.close()
        else:
            min_score = min(list(map(int, all_scores)))
            if min_score < user.score:
                copied = []
                copied.append(f'{user.name}: {user.score} ({score_data})\n')
                for line in lines:
                    if min_score != int(list(line.split())[1]):
                        copied.append(line)
                file.close()
                with open('scores.txt', 'w') as filee:
                    filee.write(''.join(sorted(copied, reverse = True,
                        key=lambda x: int(list(x.split())[1]))))

#when computer has no hp
class EnemyDown(Exception):

    def __str__(self): #repr for traceback
        return 'the enemy is down'

class CommandException(Exception): #entering unknown commands

    def __str__(self):
        return 'unknown command'


class WrongHeroException(Exception):

    def __str__(self):
        return 'wrong number of hero'
