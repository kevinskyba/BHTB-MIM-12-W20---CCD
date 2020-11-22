import math

import numpy as np

from qango.token import token
from qango.win_conditions import generate_win_conditions


class GameState:

    def __init__(self, board, current_player):
        self.board = board
        self.token = token()
        self.winners = generate_win_conditions()
        self.currentPlayer = current_player
        self.id = self._id()
        self.allowedActions = self._allowed_actions()
        self.isGameFinished = self._is_game_finished()
        self.gameWinner = self._game_winner()

    def _id(self):
        player_position = np.zeros(len(self.board), dtype=np.int)
        player_position[self.board == 1] = 1

        other_position = np.zeros(len(self.board), dtype=np.int)
        other_position[self.board == -1] = 1

        position = np.append(player_position, other_position)
        _id = ''.join(map(str, position))

        return _id

    def _allowed_actions(self):
        allowed = []
        for i in range(len(self.board)):
            if self.board[i] == 0:
                allowed.append(i)
        return allowed

    def _is_game_finished(self):
        if np.count_nonzero(self.board) == 36:
            return 1

        for a in self.winners:
            l = list(map(lambda x: self.board[x], a))
            win_condition = len(l) * -self.currentPlayer
            if np.sum(l) == win_condition:
                return 1

        return 0

    def _game_winner(self):
        if self.isGameFinished:
            for a in self.winners:
                l = list(map(lambda x: self.board[x], a))
                win_condition_player_1 = len(l)
                win_condition_player_2 = len(l) * -1
                if np.sum(l) == win_condition_player_1:
                    return 1
                elif np.sum(l) == win_condition_player_2:
                    return -1
            return 0
        return None

    def do_action(self, action):
        new_board = np.array(self.board)
        if new_board[action] != 0:
            raise Exception('Turn {0} is not allowed for player {1}'.format(action, self.currentPlayer))
        new_board[action] = self.currentPlayer

        new_state = GameState(new_board, -self.currentPlayer)

        return new_state

    def render(self, logger):
        logger.info('----------------------')
        for y in range(0, 6):
            logger.info("{0} {1} {2} {3} {4} {5}".format(self.board[y*6], self.board[y*6+1], self.board[y*6+2],
                                                         self.board[y*6+3], self.board[y*6+4], self.board[y*6+5]))
        logger.info('----------------------')
