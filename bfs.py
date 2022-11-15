from copy import deepcopy

from board import *
from cosntants import *

def move_up(p_b, c_b, zero_index, pq, visited_boards):
    if zero_index >= BOARD_LENGTH:
        c_b[zero_index], c_b[zero_index - BOARD_LENGTH] = c_b[zero_index - BOARD_LENGTH], c_b[zero_index]
        curr_board_string = numpy_array_to_string(c_b)

        if curr_board_string not in visited_boards.keys():
            pq.append(curr_board_string)
            visited_boards[curr_board_string] = numpy_array_to_string(p_b)

def move_down(p_b, c_b, zero_index, pq, visited_boards):
    if zero_index < BOARD_LENGTH * (BOARD_LENGTH - 1):
        c_b[zero_index], c_b[zero_index + BOARD_LENGTH] = c_b[zero_index + BOARD_LENGTH], c_b[zero_index]
        curr_board_string = numpy_array_to_string(c_b)

        if curr_board_string not in visited_boards.keys():
            pq.append(curr_board_string)
            visited_boards[curr_board_string] = numpy_array_to_string(p_b)

def move_left(p_b, c_b, zero_index, pq, visited_boards):
    if zero_index % BOARD_LENGTH >= 1:
        c_b[zero_index], c_b[zero_index - 1] = c_b[zero_index - 1], c_b[zero_index]
        curr_board_string = numpy_array_to_string(c_b)

        if curr_board_string not in visited_boards.keys():
            pq.append(curr_board_string)
            visited_boards[curr_board_string] = numpy_array_to_string(p_b)

def move_right(p_b, c_b, zero_index, pq, visited_boards):
    if zero_index % BOARD_LENGTH < BOARD_LENGTH - 1:
        c_b[zero_index], c_b[zero_index + 1] = c_b[zero_index + 1], c_b[zero_index]
        curr_board_string = numpy_array_to_string(c_b)

        if curr_board_string not in visited_boards.keys():
            pq.append(curr_board_string)
            visited_boards[curr_board_string] = numpy_array_to_string(p_b)


def get_final_path(curr_board, visited_boards):
    if curr_board == 'START':
        return
    else:
        get_final_path(visited_boards[curr_board], visited_boards)
        b = Board(curr_board)
        b.print_board()
        print("Board cost: ")
        print(b.board_heuristic())
        print('')

def bfs(init_board):
    # using queue for the bfs algorithm
    pq = []
    visited_boards = {}  # key is the current board string and the value is the parent board string

    new_board = Board(init_board)
    visited_boards[new_board.board_string] = 'START'

    pq.append(new_board.board_string)

    while len(pq) != 0:
        vert = pq.pop(0)
        # print(vert)
        if vert == GOAL_BOARD_STRING:
            get_final_path(GOAL_BOARD_STRING, visited_boards)
            print("got the solution")
            break

        curr_board_array = string_to_numpy_array(vert)

        zero_index = np.where(curr_board_array == 0)[0][0]
        # print(zero_index)

        move_up(curr_board_array, deepcopy(curr_board_array), zero_index, pq, visited_boards)
        move_down(curr_board_array, deepcopy(curr_board_array), zero_index, pq, visited_boards)
        move_left(curr_board_array, deepcopy(curr_board_array), zero_index, pq, visited_boards)
        move_right(curr_board_array, deepcopy(curr_board_array), zero_index, pq, visited_boards)




