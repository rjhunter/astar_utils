__author__ = 'rhunter'

from random import randint
import numpy as np

def random_grid(y=5, x=5, pclear=0.7):
    grid = (np.random.rand(y,x) > pclear).astype(int)
    grid[0][0] = 0 # start
    grid[y-1][x-1] = 0 # finish
    heuristic = np.array([np.arange(i,i+x) for i in range(y)])
    heuristic = np.flipud(np.fliplr(heuristic))
    return grid, heuristic


def main():
    grid, heuristic = random_grid(randint(5,20),randint(5,20))
    print('heuristic=')
    for row in heuristic:
        print(row)
    print('grid=')
    for row in grid:
        print(row)

if __name__ == '__main__':
    main()