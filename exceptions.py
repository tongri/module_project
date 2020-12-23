class GameOver(Exception):

    @staticmethod
    def __str__():
        return "The Game is over - u have no lives"


class EnemyDown(Exception):

    @staticmethod
    def __str__():
        return 'the enemy is down'

class NameException(Exception):

	@staticmethod
	def __str__():
		return 'your name mustn\'t have any spaces'

class StartException(Exception):
	pass

class WrongHeroException(Exception):
	pass