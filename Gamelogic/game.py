EMPTY = '0'
BOARD_LENGTH = 6
BOARD_WIDTH = 7


class Game:
    """
    this Class controls the game mode and its movements
    """
    ILLEGAL_MOVE = Exception('Illegal move')

    def __init__(self):
        """
        this function presents the board, the players and which player is supposed to play.
        """
        self.__board = [[EMPTY for _ in range(BOARD_WIDTH)] for _ in range(BOARD_LENGTH)]
        self.__last_added = [BOARD_LENGTH - 1] * BOARD_WIDTH
        self.__turn = 0
        self.__winner = 0
        self.__is_over = False
        self.__winner_cor = (0, 0)

    def __str__(self):
        """
        A function present and print the board's game.
        """
        board = [' '.join(self.__board[i]) for i in range(len(self.__board))]
        return '\n'.join(board)

    def player_turn(self):
        """
        this function determines which player is supposed to play.
        :return: number 1 for the first player and number 2 for the second player.
        """
        return self.__turn % 2 + 1

    def valid_coordinate(self, cor):
        (row, col) = cor
        if  (0 <= col <= BOARD_WIDTH -1) and (0<= row <= BOARD_LENGTH -1) :
            return True

        return False

    def check_win(self, cor):
        """
        this function checks checks if there are four squares that have the same disc
        :return: True if there are four squares that have the same disc, False if there aren't
        """
        (row, col) = cor
        directions = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1), (-1, 1), (1, -1)]
        for ind1, ind2 in directions:
            if self.valid_coordinate((row + 3 * ind1, col + 3 * ind2)):
                if self.__board[row][col] == self.__board[row + ind1][col + ind2] == \
                        self.__board[row + 2 * ind1][col + 2 * ind2] == self.__board[row + 3 * ind1][col + 3 * ind2]:
                    self.__winner_cor = [cor , (ind1, ind2)]
                    return True
        return False
    def winner_coordinates(self):
        return self.__winner_cor
    def valid_column(self, col):
        """
        this function checks of the column that the player wants to put in disc
        is empty and if it inside the boarders of the game.
        :param col: the column that the player select to put in disc
        :return: True if the column is valid(empty and inside the game borders), else return False
        """
        if col >= BOARD_WIDTH or col < 0:
            return False
        return self.__last_added[col] > -1

    def is_over(self):
        """
        this function checks if one of the players has won or if there is a draw
        (draw means all the coordinates are full).
        :return: True and the last coordinates which achieved the victory if there is victory,
                 True and ZERO if there is a draw and False if no one gets victory.
        """

        return (self.__last_added == [-1] * BOARD_WIDTH) or self.__is_over == True

    def make_move(self, col):
        """
        this function makes the move(puts the disc in the column that the player chose
        and that will be done if everything is legal, and the game is not over yet
        :param col: the column that the player wants to put in a disc
        """
        if not self.valid_column(col):
            return False , -1
        row = self.__last_added[col]
        self.__board[row][col] = str(self.player_turn())
        if self.check_win((row, col)):
            self.__is_over = True
            self.__winner = self.player_turn()
            return True, row
        self.__last_added[col] -= 1
        self.__turn = (self.__turn + 1) % 2
        return True , row

    def get_winner(self):
        """
        this function returns the which player has won: number 1 if the the first player won,
        number 2 if the the second player won, and ZERO if there is a draw
        (when the board is completely full and no winner)
        :return: the numbers 1,2 and 0 as explained above
        """
        return int(self.__winner)

    def get_player_at(self, cor):
        """
        this function accepts coordinate(row, col) ane returns which player put his/her disc in this coordinate.
        :param row: which row we want to check
        :param col: which column we want to check
        :return: number 1 if the disc belongs to first player number 2 if the disc belongs to second player
                and returns None if there is no disc in this coordinate.
        """
        row , col = cor
        if not self.valid_coordinate(cor) :
            raise Exception('Illegal location')  # if the coords are out of the game boards, it will print illegal pos.
        if not self.__board[row][col]:
            return
        return int(self.__board[row][col])

    def get_current_player(self):
        """
        returns the current player
        :return: number 1 for the first player and number 2 for the second player.
        """
        return self.player_turn()



