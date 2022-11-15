from copy import deepcopy

from board import *
from cosntants import *
from heapq import *

def move_up_astar(p_g, p_b, c_b, zero_index, pq, visited_boards):
    if zero_index >= BOARD_LENGTH:
        c_b[zero_index], c_b[zero_index - BOARD_LENGTH] = c_b[zero_index - BOARD_LENGTH], c_b[zero_index]
        curr_board_string = numpy_array_to_string(c_b)

        sub_board = Board(curr_board_string)
        sub_h_value = sub_board.board_heuristic()

        if curr_board_string not in visited_boards.keys():
            heappush(pq, (sub_h_value, p_g + 1, curr_board_string))
            visited_boards[curr_board_string] = [sub_h_value, p_g + 1, numpy_array_to_string(p_b)]
        else:
            if sub_h_value + visited_boards[numpy_array_to_string(p_b)][1] + 1 < visited_boards[curr_board_string][1] + visited_boards[curr_board_string][0]:
                visited_boards[curr_board_string][1] = visited_boards[numpy_array_to_string(p_b)][1] + 1
                visited_boards[curr_board_string][0] = sub_h_value
                visited_boards[curr_board_string][2] = numpy_array_to_string(p_b)
                heappush(pq, (sub_h_value, visited_boards[curr_board_string][1], curr_board_string))

def move_down_astar(p_g, p_b, c_b, zero_index, pq, visited_boards):
    if zero_index < BOARD_LENGTH * (BOARD_LENGTH - 1):
        c_b[zero_index], c_b[zero_index + BOARD_LENGTH] = c_b[zero_index + BOARD_LENGTH], c_b[zero_index]
        curr_board_string = numpy_array_to_string(c_b)

        sub_board = Board(curr_board_string)
        sub_h_value = sub_board.board_heuristic()

        if curr_board_string not in visited_boards.keys():
            heappush(pq, (sub_h_value, p_g + 1, curr_board_string))
            visited_boards[curr_board_string] = [sub_h_value, p_g + 1, numpy_array_to_string(p_b)]
        else:
            if sub_h_value + visited_boards[numpy_array_to_string(p_b)][1] + 1 < visited_boards[curr_board_string][1] + \
                    visited_boards[curr_board_string][0]:
                visited_boards[curr_board_string][1] = visited_boards[numpy_array_to_string(p_b)][1] + 1
                visited_boards[curr_board_string][0] = sub_h_value
                visited_boards[curr_board_string][2] = numpy_array_to_string(p_b)
                heappush(pq, (sub_h_value, visited_boards[curr_board_string][1], curr_board_string))

def move_left_astar(p_g, p_b, c_b, zero_index, pq, visited_boards):
    if zero_index % BOARD_LENGTH >= 1:
        c_b[zero_index], c_b[zero_index - 1] = c_b[zero_index - 1], c_b[zero_index]
        curr_board_string = numpy_array_to_string(c_b)

        sub_board = Board(curr_board_string)
        sub_h_value = sub_board.board_heuristic()

        if curr_board_string not in visited_boards.keys():
            heappush(pq, (sub_h_value, p_g + 1, curr_board_string))
            visited_boards[curr_board_string] = [sub_h_value, p_g + 1, numpy_array_to_string(p_b)]
        else:
            if sub_h_value + visited_boards[numpy_array_to_string(p_b)][1] + 1 < visited_boards[curr_board_string][1] + \
                    visited_boards[curr_board_string][0]:
                visited_boards[curr_board_string][1] = visited_boards[numpy_array_to_string(p_b)][1] + 1
                visited_boards[curr_board_string][0] = sub_h_value
                visited_boards[curr_board_string][2] = numpy_array_to_string(p_b)
                heappush(pq, (sub_h_value, visited_boards[curr_board_string][1], curr_board_string))

def move_right_astar(p_g, p_b, c_b, zero_index, pq, visited_boards):
    if zero_index % BOARD_LENGTH < BOARD_LENGTH - 1:
        c_b[zero_index], c_b[zero_index + 1] = c_b[zero_index + 1], c_b[zero_index]
        curr_board_string = numpy_array_to_string(c_b)

        sub_board = Board(curr_board_string)
        sub_h_value = sub_board.board_heuristic()

        if curr_board_string not in visited_boards.keys():
            heappush(pq, (sub_h_value, p_g + 1, curr_board_string))
            visited_boards[curr_board_string] = [sub_h_value, p_g + 1, numpy_array_to_string(p_b)]
        else:
            if sub_h_value + visited_boards[numpy_array_to_string(p_b)][1] + 1 < visited_boards[curr_board_string][1] + \
                    visited_boards[curr_board_string][0]:
                visited_boards[curr_board_string][1] = visited_boards[numpy_array_to_string(p_b)][1] + 1
                visited_boards[curr_board_string][0] = sub_h_value
                visited_boards[curr_board_string][2] = numpy_array_to_string(p_b)
                heappush(pq, (sub_h_value, visited_boards[curr_board_string][1], curr_board_string))

def get_final_path(curr_board, visited_boards):
    if curr_board == 'NULL':
        return
    else:
        get_final_path(visited_boards[curr_board][2], visited_boards)
        b = Board(curr_board)
        b.print_board()

        print("g value", visited_boards[curr_board][1])
        print("h value", visited_boards[curr_board][0])
        print('')

def astar(init_board):
    # using stack for the dfs algorithm
    pq = []
    visited_boards = {}

    new_board = Board(init_board)
    new_board_h_value = new_board.board_heuristic()

    visited_boards[new_board.board_string] = [new_board_h_value, 0, 'NULL']

    heappush(pq, (new_board_h_value, 0, new_board.board_string))

    while len(pq) != 0:
        vert = heappop(pq)
        # print(vert[2])
        if vert[2] == GOAL_BOARD_STRING:
            get_final_path(GOAL_BOARD_STRING, visited_boards)
            print("got the solution")
            break

        curr_board_array = string_to_numpy_array(vert[2])

        zero_index = np.where(curr_board_array == 0)[0][0]
        # print(zero_index)

        move_up_astar(vert[1], curr_board_array, deepcopy(curr_board_array), zero_index, pq, visited_boards)
        move_down_astar(vert[1], curr_board_array, deepcopy(curr_board_array), zero_index, pq, visited_boards)
        move_left_astar(vert[1], curr_board_array, deepcopy(curr_board_array), zero_index, pq, visited_boards)
        move_right_astar(vert[1], curr_board_array, deepcopy(curr_board_array), zero_index, pq, visited_boards)

        import time
        start_time = time.time()
        main()
        print("--- %s seconds ---" % (time.time() - start_time))




