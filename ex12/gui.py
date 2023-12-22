import tkinter as tk
import tkinter.messagebox
from ai import *
from game import *
import time


class Gui:
    BALLS = {1: 'red', 2: 'yellow'}

    def __init__(self, root):
        self.__game = Game()
        self.__ai1 = AI(self.__game, 1)
        self.__ai2 = AI(self.__game, 2)
        self.__root = root
        self.__frame = tk.Frame(self.__root)
        self.__canvas = tk.Canvas(self.__root, width=710, height=800)
        self.__label = tk.Label(self.__frame)
        self.__board_image = tk.PhotoImage(file="FIAR_Board.png")
        self.__quit_button = tk.Button(self.__root, text='Exit game', command=self.__frame.quit, width=15)
        self.__quit_button.pack(side=tk.BOTTOM)
        self.__menu_image = tk.PhotoImage(file='title.png')
        self.__menu_image_label = tk.Label(self.__frame, image=self.__menu_image, height=400, width=500)
        self.build_menu()

    def build_menu(self):
        """
        This function represent the f=menu of the game and let to the players to choose what kind the want to play.
        """
        self.__frame.pack()
        self.__menu_image_label.pack(side=tk.TOP)
        self.__label.pack()
        tk.Button(self.__label, text='Pc. vs Pc.', width=15, command=self.pc_vs_pc).pack()
        tk.Button(self.__label, text='Pc. vs Pl.', width=15, command=self.pc_vs_pl).pack()
        tk.Button(self.__label, text='Pl. vs Pl.', width=15, command=self.pl_vs_pl).pack()
        tk.Button(self.__label, text='Pl. vs Pc.', width=15, command=self.pl_vs_pc).pack()

    def pl_vs_pl(self):
        """
        This function is responsible for the game between player and player
        """
        self.__menu_image_label.destroy()
        self.__label.destroy()
        self.__canvas.pack()
        self.__canvas.create_image(0, 0, anchor=tk.NW, image=self.__board_image)
        self.build_playing_buttons(lambda: self.player_move(0), lambda: self.player_move(1),
                                   lambda: self.player_move(2),
                                   lambda: self.player_move(3), lambda: self.player_move(4),
                                   lambda: self.player_move(5), lambda: self.player_move(6))

    def pl_vs_pc(self):
        """
        This function is responsible for the game between player and computer.
        """
        self.__menu_image_label.destroy()
        self.__label.destroy()
        self.__canvas.pack()
        self.__canvas.create_image(0, 0, anchor=tk.NW, image=self.__board_image)
        self.build_playing_buttons(lambda: self.move_pl_pc(0), lambda: self.move_pl_pc(1),
                                   lambda: self.move_pl_pc(2),
                                   lambda: self.move_pl_pc(3), lambda: self.move_pl_pc(4),
                                   lambda: self.move_pl_pc(5), lambda: self.move_pl_pc(6))

    def pc_vs_pl(self):
        """
        This function is responsible for the game between computer and player
        """
        col = self.__ai1.find_legal_move()
        self.add_ball(col)
        self.pl_vs_pc()

    def move_pl_pc(self, col):
        """
        this function makes the first move to the player, after that makes the computer do its move by calling
        find_legal_move function from the ai file.
        :param col: the column that the player wants to put his first disc in.
        """
        self.player_move(col)
        if not self.game_over():
            col = self.__ai1.find_legal_move()
            self.add_ball(col)
            self.game_over()

    def pc_vs_pc(self):
        """
        This function is responsible for the game between computer and itself.
        """
        self.__frame.destroy()
        self.__menu_image_label.destroy()
        self.__label.destroy()
        self.__canvas.pack()
        self.__canvas.create_image(0, 0, anchor=tk.NW, image=self.__board_image)

        while self.__game.get_winner() is None:
            col = self.__ai1.find_legal_move()
            self.add_ball(col)
            self.__root.update()
            time.sleep(0.5)
        self.game_over()

    def build_playing_buttons(self, c1, c2, c3, c4, c5, c6, c7):
        """
        This is appropriate button for each column.
        :param c1: first column.
        :param c2: second column.
        :param c3: third column.
        :param c4: fourth column.
        :param c5: fifth column.
        :param c6: sixth  column.
        :param c7: seventh column.
        """
        tk.Button(self.__frame, text='Col-1', width=13, fg='black', background='blue', command=c1).pack(side=tk.LEFT)
        tk.Button(self.__frame, text='Col-2', width=13, fg='black', background='blue', command=c2).pack(side=tk.LEFT)
        tk.Button(self.__frame, text='Col-3', width=13, fg='black', background='blue', command=c3).pack(side=tk.LEFT)
        tk.Button(self.__frame, text='Col-4', width=13, fg='black', background='blue', command=c4).pack(side=tk.LEFT)
        tk.Button(self.__frame, text='Col-5', width=13, fg='black', background='blue', command=c5).pack(side=tk.LEFT)
        tk.Button(self.__frame, text='Col-6', width=13, fg='black', background='blue', command=c6).pack(side=tk.LEFT)
        tk.Button(self.__frame, text='Col-7', width=13, fg='black', background='blue', command=c7).pack(side=tk.LEFT)

    def player_move(self, col):
        """
        This function uses add_ball function and game_over , and makes except if the col is full
        :param col: int
        :return: None
        """
        try:
            self.add_ball(col)
            self.game_over()
        except:
            tkinter.messagebox.showinfo('Illegal move', 'The col is full')

    def add_ball(self, col):
        self.__game.make_move(col)
        for row in range(6):
            player = self.__game.get_player_at(row, col)
            if player in self.BALLS.keys():
                self.__canvas.create_oval(15 + 100 * col, 15 + 100 * row, 97 + 100 * col, 97 + 100 * row,
                                          fill=self.BALLS[player])

    def game_over(self):
        """
        This function checks if the game is over or not , if it, it shows info
        :return: True or False
        """
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
        return False

    def specify_winner_balls(self):
        """
        This function causing the discs which achieved the victory in the player game to be distinctive
        """
        cor = self.__game.game_over()[2]
        for i in range(4):
            self.__canvas.create_oval(15 + 100 * (cor[1] + i * cor[2][1]), 15 + 100 * (cor[0] + i * cor[2][0]),
                                      97 + 100 * (cor[1] + i * cor[2][1]), 97 + 100 * (cor[0] + i * cor[2][0]), width=5)

    def play_again_or_quit(self):
        """
        This function is responsible for ending the game or asking the player if he/she wants to play again.
        """
        if tkinter.messagebox.askquestion('Game over', 'Do you want to play again?') == 'yes':
            self.__canvas.destroy()
            self.__frame.destroy()
            self.__quit_button.destroy()
            self.__init__(self.__root)
        else:
            self.__frame.quit()


if __name__ == '__main__':
    rot = tk.Tk()
    g = Gui(rot)
    rot.mainloop()
