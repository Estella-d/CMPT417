from copy import deepcopy

from board import *
from cosntants import *

def move_up_dfs(p_b, c_b, zero_index, pq, visited_boards):
    if zero_index >= BOARD_LENGTH:
        c_b[zero_index], c_b[zero_index - BOARD_LENGTH] = c_b[zero_index - BOARD_LENGTH], c_b[zero_index]
        curr_board_string = numpy_array_to_string(c_b)

        if curr_board_string not in visited_boards.keys():
            pq.append(curr_board_string)
            visited_boards[curr_board_string] = numpy_array_to_string(p_b)

def move_down_dfs(p_b, c_b, zero_index, pq, visited_boards):
    if zero_index < BOARD_LENGTH * (BOARD_LENGTH - 1):
        c_b[zero_index], c_b[zero_index + BOARD_LENGTH] = c_b[zero_index + BOARD_LENGTH], c_b[zero_index]
        curr_board_string = numpy_array_to_string(c_b)

        if curr_board_string not in visited_boards.keys():
            pq.append(curr_board_string)
            visited_boards[curr_board_string] = numpy_array_to_string(p_b)

def move_left_dfs(p_b, c_b, zero_index, pq, visited_boards):
    if zero_index % BOARD_LENGTH >= 1:
        c_b[zero_index], c_b[zero_index - 1] = c_b[zero_index - 1], c_b[zero_index]
        curr_board_string = numpy_array_to_string(c_b)

        if curr_board_string not in visited_boards.keys():
            pq.append(curr_board_string)
            visited_boards[curr_board_string] = numpy_array_to_string(p_b)

def move_right_dfs(p_b, c_b, zero_index, pq, visited_boards):
    if zero_index % BOARD_LENGTH < BOARD_LENGTH - 1:
        c_b[zero_index], c_b[zero_index + 1] = c_b[zero_index + 1], c_b[zero_index]
        curr_board_string = numpy_array_to_string(c_b)

        if curr_board_string not in visited_boards.keys():
            pq.append(curr_board_string)
            visited_boards[curr_board_string] = numpy_array_to_string(p_b)


def get_final_path(curr_board, visited_boards):
    if curr_board == 'NULL':
        return
    else:
        get_final_path(visited_boards[curr_board], visited_boards)
        b = Board(curr_board)
        b.print_board()
        print('')

def dfs(init_board):
    # using stack for the dfs algorithm
    pq = []
    visited_boards = {}

    new_board = Board(init_board)
    visited_boards[new_board.board_string] = 'NULL'

    pq.append(new_board.board_string)

    while len(pq) != 0:
        vert = pq.pop()
        # print(vert)
        if vert == GOAL_BOARD_STRING:
            get_final_path(GOAL_BOARD_STRING, visited_boards)
            print("got the solution")
            break

        curr_board_array = string_to_numpy_array(vert)

        zero_index = np.where(curr_board_array == 0)[0][0]
        # print(zero_index)

        move_up_dfs(curr_board_array, deepcopy(curr_board_array), zero_index, pq, visited_boards)
        move_down_dfs(curr_board_array, deepcopy(curr_board_array), zero_index, pq, visited_boards)
        move_left_dfs(curr_board_array, deepcopy(curr_board_array), zero_index, pq, visited_boards)
        move_right_dfs(curr_board_array, deepcopy(curr_board_array), zero_index, pq, visited_boards)




