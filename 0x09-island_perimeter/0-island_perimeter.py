#!/usr/bin/python3
''' Island Perimeter'''


def island_perimeter(grid):
    '''Get the number of rows and columns in grid'''
    num_rows = len(grid)
    num_cols = len(grid[0])

    perimeter = 0
    for row in range(num_rows):
        for col in range(num_cols):
            # Check if the current cell is land
            if grid[row][col] == 1:
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                if row == num_rows - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                if col == num_cols - 1 or grid[row][col + 1] == 0:
                    perimeter += 1

    return perimeter
