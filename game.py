from exceptions import EnemyDown, GameOver, CommandException
from models import Player, Enemy
import datetime as dt
import settings


def main():

    try:

        name = input("Enter your name: \n").strip()

        if " " in name:
            name = name.replace(' ', '_')
            print(name)

        while True:
            command = input("Enter start, exit, show scores or help\n").strip().lower()

            if command == 'start':
                
                user = Player(name, settings.HP, settings.SCORE, settings.ALLOWED_ATTACK)
                enemy = Enemy(settings.ENEMY_LEVEL)

                print(f'Enemy level is {settings.ENEMY_LEVEL}\n')

                while True:
                    try:
                        if user.allowed_attack:
                            user.attack(enemy)
                            user.allowed_attack = 0
                        else:
                            user.allowed_attack = 1
                            user.defense(enemy)
                    except EnemyDown as err:
                        print("Creating new enemy")
                        settings.ENEMY_LEVEL += 1
                        enemy = Enemy(settings.ENEMY_LEVEL)
                        print(f'Enemy level is {settings.ENEMY_LEVEL}\n')
                        user.allowed_attack = 1
                        user.score += 5
                        print(err)

            elif command == 'show scores':
                with open('scores.txt', 'r') as file:
                    for line in file:
                        print(line, end='')
                        print('-'*10)

            elif command == 'help':
                for key in settings.COMMS.keys():
                    print(f'command {key} {settings.COMMS[key]}')

            elif command == 'exit':
                raise KeyboardInterrupt

            else:
                print(f'unknown commad {command}')




    except GameOver as err:
        err.write_score(user)

    finally:
        print('goodbye')


if __name__ == '__main__':
    main()
