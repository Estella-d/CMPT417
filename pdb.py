from collections import deque
import os.path
import json


class Pdb:

    def __init__(self, target_pattern):
        self.target = target_pattern
        self.n = target_pattern.n
        self.data = {}

    def __repr__(self):
        rep = ''
        for k, v in self.data.items():
            rep += '%s : %3d' % (k, v) + '\n'
        return rep

    def setup_pdb(self, new=False):
        file_name = './pattern_database_{}.txt'.format(self.n)
        if not os.path.isfile(file_name) or new:
            self.bfs()
            with open(file_name, 'w') as file:
                json.dump(self.data, file, indent=2)
        else:
            with open(file_name, 'r') as file:
                self.data = json.load(file)
        print("Pattern database has been loaded!")


    def get_heuristic(self, state):
        SIZE = len(state.board)
        distinguibles = self.target.distinguish
        lista = []
        for i in range(SIZE):
            for j in range(SIZE):
                if int(state.board[i][j]) in distinguibles:
                    lista.append(int(state.board[i][j]))
                else:
                    lista.append('X')
        return self.data[repr(lista)]


    def bfs(self):
        print("Preparing pattern database! . . . .")
        my_queue = deque()
        self.target.distance = 0
        self.data[self.target.to_string()] = 0
        my_queue.append(self.target)

        while my_queue:
            current = my_queue.popleft()
            for child in current.get_children():
                if not child.to_string() in self.data:
                    child.distance = current.distance + 1
                    self.data[child.to_string()] = child.distance
                    my_queue.append(child)
