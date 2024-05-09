import numpy as np

from Deterministic_V_Value.Constants import START, BOARD_ROWS, BOARD_COLUMNS, DETERMINISTIC, WIN_STATE, LOSE_STATE


# Define Board & State

class State:
    def __init__(self, state=START):
        self.board = np.zeros([BOARD_ROWS, BOARD_COLUMNS])
        self.board[1, 1] = -1
        self.state = state
        self.isEnd = False
        self.determine = DETERMINISTIC

    def give_reward(self):
        if self.state == WIN_STATE:
            return 1
        elif self.state == LOSE_STATE:
            return -1
        else:
            return 0

    def isEndFunc(self):
        if self.state == WIN_STATE or self.state == LOSE_STATE:
            self.isEnd = True

    def next_position(self, action):
        if action == "up":
            nextState = (self.state[0] - 1, self.state[1])
        elif action == "down":
            nextState = (self.state[0] + 1, self.state[1])
        elif action == "left":
            nextState = (self.state[0], self.state[1] - 1)
        else:
            nextState = (self.state[0], self.state[1] + 1)

        # verify if next state is valid
        if 0 <= nextState[0] <= BOARD_ROWS - 1:
            if 0 <= nextState[1] <= BOARD_COLUMNS - 1:
                if nextState != (1, 1):
                    return nextState

        return self.state

    def show_board(self):
        self.board[self.state] = 1
        for i in range(0, BOARD_ROWS):
            print('-------------------------------------------------------------------')
            out = '| '
            for j in range(0, BOARD_COLUMNS):
                if self.board[i, j] == 1:
                    token = '*'
                if self.board[i, j] == -1:
                    token = 'z'
                if self.board[i, j] == 0:
                    token = '0'
                out += (token + ' | ')
            print(out)
        print('-------------------------------------------------------------------')
