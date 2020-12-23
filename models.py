import random as rand
from exceptions import EnemyDown, GameOver, WrongHeroException


class Enemy:
    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        return rand.randint(1, 2)

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown


class Player:
    def __init__(self, name, lives, score, allowed_attack):
        self.name = name
        self.lives = lives
        self.score = score
        self.allowed_attack = allowed_attack

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise GameOver

    @staticmethod
    def fight(attack, defense):
        if defense - attack == 1 or defense - attack == 2:
            return 1
        elif not defense - attack:
            return 0
        else:
            return -1

    @staticmethod
    def show_soldier(who, piece):
        if piece == 1:
            print(f"{who}'s choice is magician\n")
        elif piece == 2:
            print(f"{who}'s choice is warrior\n")
        else:
            print(f"{who}'s choice is robber\n")

    def attack(self, enemy_obj):
        print("Now its time to attack\n")
        
        attacker = int(input("Enter your choice of soldiers(1, 2 or 3): ").strip())

        if attacker not in range(1, 4):
            raise WrongHeroException(f'U r only able to choose 1, 2 or 3. {attacker} is wrong number')

        Player.show_soldier(self.name, attacker)
        defencer = Enemy.select_attack()
        Player.show_soldier('Computer', defencer)
        if Player.fight(attacker, defencer) == 1:
            print('Great choice')
            enemy_obj.decrease_lives()
        elif Player.fight(attacker, defencer) == 0:
            print('Its draw')

        else:
            print('You missed')

    def defense(self, enemy_obj):
        print('Now its time to defense\n')
        defender = int(input("Enter your choice of soldiers(1, 2 or 3): "))

        if defender not in range(1, 4):
            raise WrongHeroException

        Player.show_soldier(self.name, defender)
        attacker = Enemy.select_attack()
        Player.show_soldier('Computer', attacker)
        if Player.fight(attacker, defender) == 1:
            print('You missed!')
            self.decrease_lives()
        elif  Player.fight(attacker, defender) == 0:
            print('Its draw')

        else:
            print('Great choice')


if __name__ == '__main__':
    print('ok')

