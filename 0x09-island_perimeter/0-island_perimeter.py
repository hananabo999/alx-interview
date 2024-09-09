#!/usr/bin/python3
"""island perimeter Module"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all four sides (up, down, left, right)
                if i == 0 or grid[i-1][j] == 0:  # Top side
                    perimeter += 1
                if i == rows - 1 or grid[i+1][j] == 0:  # Bottom side
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:  # Left side
                    perimeter += 1
                if j == cols - 1 or grid[i][j+1] == 0:  # Right side
                    perimeter += 1

    return perimeter
