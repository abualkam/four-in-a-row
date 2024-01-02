
"""
This file gathers all parts of the game
"""

from Gamegui.gui import *
if __name__ == '__main__':
    menu = Menu()
    menu.mainloop()
    board = Board(Game())
    board.mainloop()
    while board.play_again():
        board = Board(Game())
        board.mainloop()

