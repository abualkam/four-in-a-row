import random


class AI:
    """
    A class that responsible for the computer legal moves moves
    """

    def __init__(self, game, player):
        """

        :param game: the board game
        :param player: one of the players
        """
        self.__game = game
        self.__player = player

    def find_legal_move(self):
        """
        This function checks which column is valid to put in disc (where the player can make move.
        :return: A randomly number from the valid column list.
        """
        result = []
        for col in range(7):
            for row in range(5, -1, -1):
                if self.__game.get_player_at(row, col) is None:
                    result.append(col)
                    break
        return random.choice(result)   # calling random library to get a randomly element form the column list.

    def get_last_found_move(self):
        pass
