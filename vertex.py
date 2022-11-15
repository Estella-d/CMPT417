
class Vertex:
    def __init__(self, curr_board, parent_board, h_value, total_cost):
        self.curr_board = curr_board
        self.parent_board = parent_board
        self.h_value = h_value
        self.total_cost = total_cost