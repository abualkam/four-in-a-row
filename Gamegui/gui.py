import tkinter as tk
import tkinter.messagebox

from Gamelogic.game import Game


class Menu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Four in a row")
        self.__menu_frame = tk.Frame(self)
        self.__menu_image = tk.PhotoImage(file='./Gamegui/Menu_image.png')
        self.__menu_frame.pack()
        image_label = tk.Label(self.__menu_frame, image=self.__menu_image, height=400, width=500)
        image_label.pack(side=tk.TOP)
        buttons_label = tk.Label(self.__menu_frame)
        buttons_label.pack()
        tk.Button(buttons_label, text='Start game', width=15, command=lambda: self.destroy()).pack()


class Board(tk.Tk):
    BALLS = {1: 'red', 2: 'yellow'}

    def __init__(self, game: Game):
        super().__init__()
        self.title("Four in a row")
        self.__play_again = False
        self.__game = game
        self.__canvas = tk.Canvas(self, width=710, height=600)
        self.__label = tk.Label(self)
        self.__board_image = tk.PhotoImage(file='./Gamegui/Board_image.png')
        self.__canvas.create_image(0, 0, anchor=tk.NW, image=self.__board_image)
        self.build_buttons()
        self.__label.pack()
        self.__canvas.pack()

    def build_buttons(self):
        for i in range(7):
            tk.Button(self.__label, text=f'Col-{i}', width=13, fg='black', background='blue',
                      command=lambda i=i: self.set_user_input(i)).pack(
                side=tk.LEFT)

    def set_user_input(self, col):
        valid_move, row = self.__game.make_move(col)
        if not valid_move:
            tkinter.messagebox.showinfo('Column is full', 'Try another one')
            return
        self.draw_ball((row, col))
        if self.__game.is_over():
            winner = self.__game.get_winner()
            if winner == 0:
                tkinter.messagebox.showinfo('Game over', 'Board is full')
                self.play_again_or_quit()
                return True
            elif winner == 1 or winner == 2:
                self.specify_winner_balls()
                tkinter.messagebox.showinfo('Game over', 'Player with ' + self.BALLS[winner] + ' ball has won')
                self.play_again_or_quit()
                return True

    def draw_ball(self, cor):
        row, col = cor
        player = self.__game.get_player_at(cor)
        if player in self.BALLS.keys():
            self.__canvas.create_oval(15 + 100 * col, 15 + 100 * row, 97 + 100 * col, 97 + 100 * row,
                                      fill=self.BALLS[player])

    def specify_winner_balls(self):
        """
        This function causing the discs which achieved the victory in the player game to be distinctive
        """
        cor = self.__game.winner_coordinates()
        for i in range(4):
            self.__canvas.create_oval(15 + 100 * (cor[0][1] + i * cor[1][1]), 15 + 100 * (cor[0][0] + i * cor[1][0]),
                                      97 + 100 * (cor[0][1] + i * cor[1][1]), 97 + 100 * (cor[0][0] + i * cor[1][0]),
                                      width=5)

    def play_again_or_quit(self):
        """
        This function is responsible for ending the game or asking the player if he/she wants to play again.
        """
        if tkinter.messagebox.askquestion('Game over', 'Do you want to play again?') == 'yes':
            self.__play_again = True
        self.destroy()

    def play_again(self):
        return self.__play_again
