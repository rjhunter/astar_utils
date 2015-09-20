__author__ = 'rhunter'

import sys
from random import randint
from io import StringIO
import numpy as np

def random_grid(y=5, x=5, pclear=0.7):
    """Produce a random grid of specified dimensions.

    :param y: number of rows
    :param x: number of columns
    :param pclear: probability that a given cell is clear
    :return: randomized grid
    """
    grid = (np.random.rand(y,x) > pclear).astype(int)
    grid[0][0] = 0 # start
    grid[y-1][x-1] = 0 # finish
    heuristic = np.array([np.arange(i,i+x) for i in range(y)])
    heuristic = np.flipud(np.fliplr(heuristic))
    return grid, heuristic

def print_grid(grid, fout=sys.stdout):
    """ Pretty-print a grid

    :param grid: what to print
    :param fout: file handle to print to
    """
    grid_str = [[str(c) for c in r] for r in grid]
    maxw = max([len(c) for r in grid_str for c in r])
    fmt = ' {{:{:d}s}}'.format(maxw)
    for r in grid_str:
        print('[', end='', file=fout)
        for c in r:
            print(fmt.format(c), end='', file=fout)
        print(' ]', file=fout)
    print()

def print_grids(grids):
    """ Pretty print several grids side-by-side

    :param grids: what to print
    """
    ss = [StringIO("") for _ in range(len(grids))]
    for v, s in zip(grids, ss):
        print_grid(v, fout=s)
    ss = [s.getvalue().split('\n')[:-1] for s in ss]
    for rows in zip(*ss):
        print('|'.join(rows))
    print()

def visual_grid(grid, init=None, goal=None):
    """ Convert a grid of ones and zeros to something nicer.

    :param grid: what to convert
    :param init: optional start location
    :param goal: optional finish location
    :return: converted grid
    """
    vgrid = [[' ' for c in r] for r in grid]
    nrow = len(grid)
    ncol = len(grid[0])
    for y in range(nrow):
        for x in range(ncol):
            if (y,x) == init:
                vgrid[y][x] = u'\u2605'
            elif (y,x) == goal:
                vgrid[y][x] = u'\u2691'
            elif grid[y][x] == 1:
                vgrid[y][x] = u'\u2588'
            else:
                vgrid[y][x] = u'\u2591'
    return vgrid

def main():
    grid, heuristic = random_grid(randint(5,20),randint(5,20))
    print('heuristic=')
    print_grid(heuristic)
    print('grid=')
    print_grid(grid)

if __name__ == '__main__':
    main()