'''
You are given an M by N matrix consisting of booleans that represents a board.
Each True boolean represents a wall. Each False boolean represents
a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate,
return the minimum number of steps required to reach the end coordinate
from the start. If there is no possible path, then return null.
You can move up, left, down, and right. You cannot move through walls.
You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
 [t, t, f, t],
 [f, f, f, f],
 [f, f, f, f]]

and start = (3, 0) (bottom left) and end = (0, 0) (top left),
the minimum number of steps required to reach the end is 7,
since we would need to go through (1, 2) because there is a wall
everywhere else on the second row.
'''

def walk_board(board, start, end):
    
    sx = start[0]
    sy = start[1]
    ex = end[0]
    ey = end[1]

    if board[sx][sy] == False or board[ex][ey] == True:
        return None

    steps = 0

    currx = sx
    cuury = sy

    while currx != ex or curry != ey:
        short = check_shortest(matrix, curr, end)

        # TODO: idea is to turn the tile to true if it has been visited

# helper function that returns the shortest next step (left, right, up or down)
# returns the string 'left', 'right', 'up', 'down'
def check_shortest(matrix, curr, end):

    left = 0
    right = 0
    up = 0
    down = 0
    for i in range(len(matrix)):
        # TODO:
    

# TESTCASES
f = False
t = True
matrix = [[f, f, f, f],
          [t, t, f, t],
          [f, f, f, f],
          [f, f, f, f]]
walk_board(matrix, start, end)
