# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from board import *
from bfs import *
from dfs import *
from astar import *
import time
from typing import Callable
import psutil
import os

from ida2 import ida
from pdb import Pdb
from slider import AbstractBoard
from slider import  Board as bd
class TimeCounter(object):
    @staticmethod
    def count_actual_running_time(func: Callable, parameter = '1,2,3,4,5,6,7,8,13,9,12,15,0,11,10,14'):
        start = time.time()
        if isinstance(parameter,tuple):
            func(*parameter)
        else:
            func(parameter)
        end = time.time()
        return end-start

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    b = Board('1,2,3,4,5,6,7,8,13,9,12,15,0,11,10,14')
    b.print_board()
    print("\nTest bfs solution")

    # bfs_duration = TimeCounter.count_actual_running_time(func=bfs,parameter="1,2,3,4,5,6,7,8,0,10,11,12,9,13,14,15")
    # dfs_duration = TimeCounter.count_actual_running_time(func=dfs,parameter="1,2,3,4,5,6,7,8,0,10,11,12,9,13,14,15")
    # astar_duration = TimeCounter.count_actual_running_time(func=astar,parameter="1,2,3,4,5,6,7,8,0,10,11,12,9,13,14,15")
    #
    # print(bfs_duration)
    # print(dfs_duration)
    # print(astar_duration)



    # print('\nTest dfs solution')
    # # dfs('1,2,3,4,5,6,7,8,13,9,12,15,0,11,10,14')
    # dfs('1,2,3,4,5,6,7,8,0,10,11,12,9,13,14,15')
    #
    # print('\nTest astar solution')
    # # astar('1,2,3,4,5,6,7,8,13,9,12,15,0,11,10,14')
    # # astar('0,12,9,13,15,11,10,14,3,7,2,5,4,8,6,1')
    # # astar('0,12,10,13,15,11,14,9,3,7,2,5,4,8,6,1')
    # astar('0,12,9,13,15,11,10,14,7,8,5,6,4,3,2,1')

    print('\nTest pdb solution')
    number_of_solution = 1
    t0 = AbstractBoard(0, 1)
    t1 = AbstractBoard(1, 1)
    t2 = AbstractBoard(2, 1)
    t3 = AbstractBoard(3, 1)
    t0.make_target_pattern()
    t1.make_target_pattern()
    t2.make_target_pattern()
    t3.make_target_pattern()
    pdb0 = Pdb(t0)
    pdb1 = Pdb(t1)
    pdb2 = Pdb(t2)
    pdb3 = Pdb(t3)
    pdb0.setup_pdb(1)
    pdb1.setup_pdb(1)
    pdb2.setup_pdb(1)
    pdb3.setup_pdb(1)

    bd.pdbs4.append(pdb0)
    bd.pdbs4.append(pdb1)
    bd.pdbs4.append(pdb2)
    bd.pdbs4.append(pdb3)
    for i in range(number_of_solution):
        s = bd()
        pat = '1,2,3,4,5,6,7,8,0,10,11,12,9,13,14,15'
        goal = "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0"
        s = s.init_state(pat,goal)
        print("Experiment %2d: \n" % i)
        print(s)
        ida(s, 2)
        idastar_duration = TimeCounter.count_actual_running_time(func=ida,
                                                               parameter=(s,2))
        print(idastar_duration)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(psutil.Process(os.getpid()).memory_info().rss)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

