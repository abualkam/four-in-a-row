class Game:
    """
    this Class controls the game mode and its movements
    """
    ILLEGAL_MOVE = Exception('Illegal move')

    def __init__(self):
        """
        this function presents the board, the players and which player is supposed to play.
        """
        self.__board = [[0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0]]
        self.__player1 = 1
        self.__player2 = 2
        self.__turn = 0

    def print_board(self):
        """
        A function present and print the board's game.
        """
        for i in range(len(self.__board)):
            print(self.__board[i])

    def player_turn(self):
        """
        this function determines which player is supposed to play.
        :return: number 1 for the first player and number 2 for the second player.
        """
        if self.__turn % 2 == 0:
            return 1
        return 2

    def board_boarders(self):
        """
        this function represent the board as a coordinates.
        :return: each square in the board and its coordinate.
        """
        boarders = []
        for row in range(len(self.__board)):
            for col in range(len(self.__board[0])):
                boarders.append((row, col))
        return boarders

    def check_coordinate(self, row, col, ind1, ind2):
        """
        this function checks checks if there are four squares that have the same disc
        :return: True if there are four squares that have the same disc, False if there aren't
        """
        boarders = self.board_boarders()
        if (row + 3*ind1, col+3*ind2) in boarders:
            if self.__board[row][col] == self.__board[row+ind1][col+ind2] ==\
                    self.__board[row+2*ind1][col+2*ind2] == self.__board[row+3*ind1][col+3*ind2]:
                return True
        return False

    def valid_col(self, col):
        """
        this function checks of the column that the player wants to put in disc
        is empty and if it inside the boarders of the game.
        :param col: the column that the player select to put in disc
        :return: True if the column is valid(empty and inside the game borders), else return False
        """
        if col > len(self.__board[0]) - 1 or col < 0:
            return False
        counter = 0
        for row in range(len(self.__board)):
            if self.__board[row][col]:
                counter += 1
        if counter == len(self.__board):
            return False
        return True

    def game_over(self):
        """
        this function checks if one of the players has won or if there is a draw
        (draw means all the coordinates are full).
        :return: True and the last coordinates which achieved the victory if there is victory,
                 True and ZERO if there is a draw and False if no one gets victory.
        """
        list_of_ind = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1), (-1, 1), (1, -1)]
        counter = 0
        for row in range(len(self.__board)):
            for col in range(len(self.__board[0])):
                if self.__board[row][col]:
                    counter += 1
                    for tup in list_of_ind:
                        if self.check_coordinate(row, col, tup[0], tup[1]):
                            return True, self.__board[row][col], (row, col, tup)
        if counter == len(self.__board)*len(self.__board[0]):
            return True, 0
        return False,

    def make_move(self, column):
        """
        this function makes the move(puts the disc in the column that the player chose
        and that will be done if everything is legal, and the game is not over yet
        :param column: the column that the player wants to put in a disc
        """
        if self.game_over()[0] or not self.valid_col(column):
            raise Exception('Illegal move')
        for row in range(-1, -(len(self.__board)+1), -1):
            if not self.__board[row][column]:
                self.__board[row][column] = self.player_turn()
                self.__turn += 1  # here we change the turn to the second player
                return

    def get_winner(self):
        """
        this function returns the which player has won: number 1 if the the first player won,
        number 2 if the the second player won, and ZERO if there is a draw
        (when the board is completely full and no winner)
        :return: the numbers 1,2 and 0 as explained above
        """
        game_over = self.game_over()
        if game_over[0]:
            return game_over[1]

    def get_player_at(self, row, col):
        """
        this function accepts coordinate(row, col) ane returns which player put his/her disc in this coordinate.
        :param row: which row we want to check
        :param col: which column we want to check
        :return: number 1 if the disc belongs to first player number 2 if the disc belongs to second player
                and returns None if there is no disc in this coordinate.
        """
        boarders = self.board_boarders()
        if (row, col) not in boarders:
            raise Exception('Illegal location')  # if the coords are out of the game boards, it will print illegal pos.
        if not self.__board[row][col]:
            return
        return self.__board[row][col]

    def get_current_player(self):
        """
        returns the current player
        :return: number 1 for the first player and number 2 for the second player.
        """
        return self.player_turn()
