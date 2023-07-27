#!/usr/bin/python3
"""0x1C-island_perimeter"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    num = 0
    rows = len(grid)
    cols = len(grid[0])

    def is_water(x, y):
        return x < 0 or y < 0 or x >= rows or y >= cols or grid[x][y] == 0

    for column in range(rows):
        for row in range(cols):
            if grid[column][row] == 1:
                num += is_water(column - 1, row)
                num += is_water(column + 1, row)
                num += is_water(column, row + 1)
                num += is_water(column, row - 1)

    return num
