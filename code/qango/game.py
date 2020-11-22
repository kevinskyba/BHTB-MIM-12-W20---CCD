import numpy as np
import loggers

from qango.game_state import GameState
from qango.token import token
from qango.win_conditions import generate_win_conditions


# The board is represented like this:
#  0  1  2  3  4  5
#  6  7  8  9 10 11
# 12 13 14 15 16 17
# 18 19 20 21 22 23
# 24 25 26 27 28 29
# 30 31 32 33 34 35
class Game:

    def __init__(self, initial_player=1):
        self.currentPlayer = initial_player
        self.token = token()
        self.gameState = GameState(np.zeros(36, dtype=np.int), self.currentPlayer)
        self.gridShape = (6, 6)
        self.inputShape = (2, 6, 6)

    def reset(self):
        self.currentPlayer = 1
        self.gameState = GameState(np.zeros(36, dtype=np.int), self.currentPlayer)

    def step(self, action):
        next_state = self.gameState.do_action(action)
        self.gameState = next_state
        self.currentPlayer = -self.currentPlayer
        return next_state