from cosntants import *
import numpy as np


class Board:
    # board will be represented as one dimensional numpy array
    def __init__(self, bs: str):
        self.board_string = bs
        self.curr_board = string_to_numpy_array(bs)

    def __str__(self):
        return self.board_string

    def print_board(self):
        for row in range(BOARD_LENGTH):
            for col in range(BOARD_LENGTH):
                print('{:4}'.format(self.curr_board[row * BOARD_LENGTH + col]), end=' ')
            print("")

    def board_heuristic(self):
        heuristic = 0
        for row in range(BOARD_LENGTH):
            for col in range(BOARD_LENGTH):
                curr_v = self.curr_board[row * BOARD_LENGTH + col]
                if curr_v != 0:
                    goal_x = (curr_v - 1) // BOARD_LENGTH
                    goal_y = (curr_v - 1) % BOARD_LENGTH
                else:
                    goal_x = BOARD_LENGTH - 1
                    goal_y = BOARD_LENGTH - 1
                heuristic += int(abs(row - goal_x) + abs(col - goal_y))
        return heuristic


def string_to_numpy_array(board_string):
    """

    :param board_string:
    :return:
    >>> print(string_to_numpy_array('1,2,3,4,5,6,7,8'))
    [1 2 3 4 5 6 7 8]
    >>> string_to_numpy_array('1,2,3,4,5,6,7,8')
    array([1, 2, 3, 4, 5, 6, 7, 8])
    """
    board_list = [int(item) for item in board_string.split(',')]
    return np.array(board_list)


def numpy_array_to_string(board_array):
    """

    :param board_array:
    :return:
    >>> numpy_array_to_string(np.array([1, 2, 3, 4, 5, 6, 7, 8]))
    '1,2,3,4,5,6,7,8'
    """
    board_list = list(board_array)
    return ','.join([str(item) for item in board_list])
