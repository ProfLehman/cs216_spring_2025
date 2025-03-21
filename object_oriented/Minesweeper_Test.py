# MinesweeperTest.py
# prof. lehman
# spring 2025
#
# tests Minesweeper Class

from Minesweeper import *


# *** main ***

game = Minesweeper(10, 10)

print("Mines:")
print(game.to_string_mines())
print()
