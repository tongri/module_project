from exceptions import EnemyDown, GameOver, NameException, StartException
from models import Player, Enemy
import datetime as dt
import settings


def main():


    try:
        name = input("Enter your name: \n")

        if " " in name.strip():
            raise NameException

        start = input("Enter start, exit, show scores or help\n")

        if start.strip().lower() == 'start':
            
            user = Player(name, settings.HP, settings.score, settings.allowed_attack)
            enemy = Enemy(settings.enemy_level)

            print(f'Enemy level is {settings.enemy_level}\n')

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
                    settings.enemy_level += 1
                    enemy = Enemy(settings.enemy_level)
                    print(f'Enemy level is {settings.enemy_level}\n')
                    user.allowed_attack = 1
                    user.score += 5
                    print(err)

        elif start.strip().lower() == 'show scores':
            with open('scores.txt', 'r') as file:
                for line in file:
                    print(line, end='')
                    print('-'*10)

        elif start.strip().lower() == 'help':
            for key in settings.COMMS.keys():
                print(f'command {key} {settings.COMMS[key]}')

        elif start.strip().lower() == 'exit':
            raise KeyboardInterrupt




    except GameOver:
        file = open('./scores.txt', 'r+')
        lines = file.readlines()
        all_scores = [list(line.split())[1] for line in lines]
        score_data = dt.datetime.now().strftime('%Y-%m-%d %H:%M')
        if len(all_scores) > 10:
            file.write(f'{user.name}: {user.score} ({score_data})\n')
            file.close()
        else:
            min_score = min(list(map(lambda x: int(x), all_scores)))
            if min_score < user.score:
                copied = []
                copied.append(f'{user.name}: {user.score} ({score_data})\n')
                for line in lines:
                    if min_score != int(list(line.split())[1]):
                        copied.append(line)
                file.close()
                with open('scores.txt', 'w') as filee:
                    filee.write(''.join(sorted(copied, reverse = False, key=lambda x: list(x.split()[1]))))


    finally:
        print('goodbye')


if __name__ == '__main__':
    main()
