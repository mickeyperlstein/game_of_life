"""
Problem statement:

Given a board with m by n cells, each cell has an initial state live (1) or
dead (0). Each cell interacts with its eight neighbors (horizontal, vertical,
diagonal) using the following four rules :

1. Any live cell with fewer than two live neighbors dies, as if caused by
under-population.

2. Any live cell with two or three live neighbors lives on to the next
generation.

3. Any live cell with more than three live neighbors dies, as if by
over-population..

4. Any dead cell with exactly three live neighbors becomes a live cell, as if
by reproduction.

Write a function to compute the next state of the board given its current
state.  The next state is created by applying the above rules simultaneously
to every cell in the current state, where births and deaths occur
simultaneously.

Example:

[             [
  [0,1,0],      [0,0,0],
  [0,0,1], ->   [1,0,1],
  [1,1,1],      [0,1,1],
  [0,0,0]       [0,1,0]
]             ]
"""
from typing import List

ALIVE = 1
DEAD = 0

import logging

logging.basicConfig()
log = logging.getLogger('').setLevel(logging.DEBUG)
logging.debug('hello im in debug')


def next_state(board: List[List[int]]) -> List[List[int]]:
    """Return the next state of the board.

    Args:
        board: The board for which the next state should be returned.
    """

    # init board
    M = len(board)
    N = len(board[0])
    ret = [0] * M
    for i, r in enumerate(ret):
        ret[i] = [0] * N

    for m in range(M):
        for n in range(N):

            alive = 0
            current_cell = board[m][n]

            # (i-1, j-1), (i-1, j) (i-1, j+1)
            # (i1, j-1), (i, j) (i, j+1)
            # (i+1, j-1), (i+1, j) (i+1, j+1)
            for i in range(-1, 1 + 1):
                for j in range(-1, 1 + 1):
                    try:

                        row_i = m + i
                        if row_i < 0 or row_i >= M:
                            continue

                        col_i = n + j
                        if col_i < 0 or col_i >= N:
                            continue

                        alive += 1 if board[row_i][col_i] == ALIVE else 0
                    except IndexError as e:
                        logging.exception(e)
                        logging.error(f'Index error, i={i}, m={m}, row_i={row_i} col_i={col_i}')


            # count how many neighbours are alive


            if current_cell == ALIVE:
                # adjust figure removing self count (i,j)
                alive -= 1

            # check if dead
            # check neighbours alive count

            if current_cell == ALIVE and alive < 2:
                ret[m][n] = DEAD
                logging.debug(f'under population, ({m},{n})')

            elif current_cell == ALIVE and alive > 3:
                ret[m][n] = DEAD
                logging.debug(f'over population, ({m},{n})')

            elif current_cell == DEAD and alive == 3:
                ret[m][n] = ALIVE
                logging.debug(f'spontaneus reporoduction, ({m},{n})')

            else:
                ret[m][n] = current_cell
    return ret

