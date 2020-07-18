import numpy as np
import math
import pandas as pd
import random
from array import *
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from random import seed
from random import randrange
from csv import reader

# region SearchAlgorithms
class Node:
    id = None
    up = None
    down = None
    left = None
    right = None
    pos_x = None
    pos_y = None
    previousNode = None

    def __init__(self, value):
        self.value = value

    def __init__(self, id, up, down, left, right, pos_x, pos_y):
        self.id = id
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.pos_x = pos_x
        self.pos_y = pos_y


class SearchAlgorithms:
    path = []  # Represents the correct path from start node to the goal node.
    fullPath = []  # Represents all visited nodes from the start node to the goal node.
    my_queue: Node = []
    Grid_Nodes: Node = []
    Board = []
    Num_of_Cols = None
    Num_of_Rows = None
    end_node_id = None
    start_node_id = None

    def __init__(self, mazeStr):

        rowlist = mazeStr.split(" ")
        self.Num_of_Rows = len(rowlist)

        for i in range(len(rowlist)):
            self.Board.append(rowlist[i].split(","))

        self.Num_of_Cols = len(self.Board[0])
        self.init_Nodes(self.Num_of_Rows, self.Num_of_Cols)

    def BFS(self):
        x, y = self.Find_Start_index()
        N = self.Grid_Nodes[x][y]
        self.my_queue.append(N)

        while len(self.my_queue) > 0:
            N = self.my_queue[0]

            if N.id == self.end_node_id:
                self.path.append(N.id)
                self.fullPath.append(N.id)
                self.GetPathFromEnd(N)
                self.path.reverse()
                return self.fullPath, self.path
            else:
                if N.id not in self.fullPath:
                    self.fullPath.append(N.id)
                    if N.up != -1:
                        up_child = self.Grid_Nodes[N.pos_x - 1][N.pos_y]
                        if up_child.id not in self.fullPath:
                            self.my_queue.append(up_child)
                            up_child.previousNode = N.id

                    if N.down != -1:
                        down_child = self.Grid_Nodes[N.pos_x + 1][N.pos_y]
                        if down_child.id not in self.fullPath:
                            self.my_queue.append(down_child)
                            down_child.previousNode = N.id

                    if N.left != -1:
                        left_child = self.Grid_Nodes[N.pos_x][N.pos_y - 1]
                        if left_child.id not in self.fullPath:
                            self.my_queue.append(left_child)
                            left_child.previousNode = N.id

                    if N.right != -1:
                        right_child = self.Grid_Nodes[N.pos_x][N.pos_y + 1]
                        if right_child.id not in self.fullPath:
                            self.my_queue.append(right_child)
                            right_child.previousNode = N.id

            self.my_queue.pop(0)

    def init_Nodes(self, Num_of_Rows, Num_of_Cols):
        id = 0
        block = "#"
        end_node = "E"
        start_node = "S"
        for i in range(Num_of_Rows):
            row = []
            for j in range(Num_of_Cols):
                find_up = -1
                find_down = -1
                find_left = -1
                find_right = -1
                if self.Board[i][j] != block:
                    if j > 0:
                        if self.Board[i][j - 1] != block:
                            find_left = 1
                    if j < self.Num_of_Cols - 1:
                        if self.Board[i][j + 1] != block:
                            find_right = 1
                    if i > 0:
                        if self.Board[i - 1][j] != block:
                            find_up = 1
                    if i < self.Num_of_Rows - 1:
                        if self.Board[i + 1][j] != block:
                            find_down = 1

                if self.Board[i][j] == end_node:
                    self.end_node_id = id
                    node = Node(self.end_node_id, find_up, find_down, find_left, find_right, i, j)
                elif self.Board[i][j] == start_node:
                    self.start_node_id = id
                    node = Node(self.start_node_id, find_up, find_down, find_left, find_right, i, j)
                else:
                    node = Node(id, find_up, find_down, find_left, find_right, i, j)

                row.append(node)
                id += 1

            self.Grid_Nodes.append(row)

    def GetPathFromEnd(self, end_node):
        while end_node.id != self.start_node_id:
            prev_node_id = self.Grid_Nodes[end_node.pos_x][end_node.pos_y].previousNode
            end_node = self.Grid_Nodes[int(prev_node_id / self.Num_of_Cols)][prev_node_id % self.Num_of_Cols]
            self.path.append(end_node.id)

    def Find_Start_index(self):
        for i in range(self.Num_of_Rows):
            for j in range(self.Num_of_Cols):
                if self.Grid_Nodes[i][j].id == self.start_node_id:
                    return i, j


# endregion
def SearchAlgorithm_Main():
    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    fullPath, path = searchAlgo.BFS()
    print('**BFS**\n Full Path is: ' + str(fullPath) + "\n Path: " + str(path))

######################## MAIN ###########################33
if __name__ == '__main__':
    SearchAlgorithm_Main()