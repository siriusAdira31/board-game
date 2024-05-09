import numpy as np

from Constants import BOARD_ROWS, BOARD_COLUMNS
from State import State


# Define Agent

class Agent:
    def __init__(self):
        self.states = []
        self.actions = ["up", "down", "left", "right"]
        self.State = State()
        self.learning_rate = 0.2
        self.exploration_rate = 0.3

        # initialize state values
        self.state_values = {}
        for row in range(0, BOARD_ROWS):
            for column in range(0, BOARD_COLUMNS):
                self.state_values[(row, column)] = 0  # initialize with 0

    def choose_action(self):
        # choose action with most expected value
        max_next_reward = 0
        action = ""

        if np.random.uniform(0, 1) <= self.exploration_rate:
            action = np.random.choice(self.actions)
        else:
            # greedy approach
            for a in self.actions:
                next_reward = self.state_values[self.State.next_position(a)]
                if next_reward >= max_next_reward:
                    action = a
                    max_next_reward = next_reward

        return action

    def take_action(self, action):
        position = self.State.next_position(action)
        self.State.state = position
        return position

    def reset(self):
        self.states = []
        self.State = State()

    def play(self, rounds=10):
        i = 0
        while i < rounds:
            if self.State.isEnd:
                # To the end -> back propagate reward
                reward = self.State.give_reward()
                # explicitly assign end state to reward values
                self.state_values[self.State.state] = reward
                print("******** Game End Reward : {} ********".format(reward))
                for s in reversed(self.states):
                    reward = self.state_values[s] + self.learning_rate * (reward - self.state_values[s])
                    self.state_values[s] = round(reward, 3)
                self.reset()
                i += 1
            else:
                action = self.choose_action()
                # add trace
                self.states.append(self.State.next_position(action))
                print("current position {} | action {}".format(self.State.state, action))
                # by taking the action, it reaches the next state
                self.take_action(action)
                # mark as end if End condition met
                self.State.isEndFunc()
                print("next state", self.State.state)
                print("______________________________________")

    def show_values(self):
        for i in range(0, BOARD_ROWS):
            print('-------------------------------------')
            out = '| '
            for j in range(0, BOARD_COLUMNS):
                out += str(self.state_values[(i, j)]).ljust(6) + ' | '
            print(out)
        print('-------------------------------------')
