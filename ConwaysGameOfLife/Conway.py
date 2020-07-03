'''
The Game of Life, also known simply as Life, is a cellular automaton devised by 
the British mathematician John Horton Conway in 1970. It is a zero-player game, 
meaning that its evolution is determined by its initial state, requiring no
further input. One interacts with the Game of Life by creating an initial 
configuration and observing how it evolves. It is Turing complete and can 
simulate a universal constructor or any other Turing machine.

Rules:
The playing field for this Game of Life is a two-dimensional orthogonal grid of 
WIDTH columns and HEIGHT rows of square cells. At any given moment in time, each 
cell is in one of two possible states, populated or unpopulated. Every cell 
interacts with its eight neighbors, which are the cells horizontally, vertically,
or diagonally adjacent. At each step in time, the following transitions occur:
   1. Any populated cell with two or three populated neighbors remains populated
   3. All other populated cells are unpopulated
   2. Any unpopulated cell with three populated neighbours is populated
   4. All other unpopulated cells stay unpopulated
The initial pattern, which is generated randomly, constitutes the seed of the
system. Each subsequent pattern is created by applying the above rules 
simultaneously to every cell in the preceding pattern, so that each pattern is a 
pure function of the preceding pattern. The rules continue to be applied 
repeatedly to create further patterns. The system continues transforming 
patterns until either no more cells remain which can be transitioned according 
to the above rules or the system begins alternating between two terminal patterns.

Conway's Game of Life.(n.d.). In Wikipedia. Retrieved August 13, 2016, from 
    https: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
'''

import random, copy, time, sys
from cursor import clearScreen, moveCursor, hideCursor, showCursor

# constants
WIDTH = 40
HEIGHT = 20
DEAD = ' '
ALIVE = '\u2588'
PAUSE_TIME = 0.1
ROW = 4
COLUMN = 8

# lambda functions
left  = lambda n: n - 1
above = lambda n: n - 1
right = lambda n: (n + 1) % HEIGHT
below = lambda n: (n + 1) % WIDTH

# functions
def boardEmpty(board):
    end = True
    for row in range(HEIGHT):
        for column in range(WIDTH):
            if board[row][column] == ALIVE: end = False
    return end

# ==============================================================================

def checkCell(board, row, column):
    count = 0
    # top row
    if board[left(row)][above(column)] == ALIVE:
        count += 1
    if board[row][above(column)] == ALIVE:
        count += 1
    if board[right(row)][above(column)] == ALIVE:
        count += 1
    # middle row 
    if board[left(row)][column] == ALIVE:
        count += 1
    if board[right(row)][column] == ALIVE:
        count += 1
    # bottom row  
    if board[left(row)][below(column)] == ALIVE:
        count += 1
    if board[row][below(column)] == ALIVE:
        count += 1
    if board[right(row)][below(column)] == ALIVE:
        count += 1
    return count

# ==============================================================================

def changeBoard(board):
    boardCopy = copy.deepcopy(board)
    for row in range(HEIGHT):
        for column in range(WIDTH):
            check = checkCell(boardCopy, row, column)
            if boardCopy[row][column] == ALIVE and (check == 2 or check == 3):
                board[row][column] = ALIVE
            elif boardCopy[row][column] == DEAD and check == 3:
                board[row][column] = ALIVE
            else:
                board[row][column] = DEAD

# ==============================================================================

def printBoard(board):
    for row in range(HEIGHT):
        moveCursor(COLUMN, ROW + row)
        for column in range(WIDTH):
            print(board[row][column], end='')
        print()
    
# ==============================================================================

def initBoard():
    board = []
    for _i in range(HEIGHT):
        column = []
        for _j in range(WIDTH):
            (column.append(ALIVE) if random.randint(0, 1) == 0 
                else column.append(DEAD))
        board.append(column)
    return board

# ===========================================================================

def main():
    try:
        clearScreen()
        hideCursor()
        board = initBoard()
        while not boardEmpty(board):
            printBoard(board)
            time.sleep(PAUSE_TIME)
            changeBoard(board)
            printBoard(board)
        print("\n\n\n")
        showCursor()
        sys.exit()
    except KeyboardInterrupt:
        print("\n\n\n")
        showCursor() 
        sys.exit()

# program entry
main()
