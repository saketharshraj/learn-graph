from data import minimum_island_size_data

def find_minimum_island_size(grid):
    visited = set()
    minimum_island_size = float("inf")
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            current_island_size = explore_island(grid, row, col, visited)
            if  0 < current_island_size < minimum_island_size:
                minimum_island_size = current_island_size
    return minimum_island_size

def explore_island(grid, row, col, visited):
    row_bound = 0 <= row < len(grid)
    col_bound = 0 <= col < len(grid[0])
    if not row_bound or not col_bound:
        return 0

    if (grid[row][col] == 'W'):
        return 0
    pos = f'{row},{col}'
    if pos in visited:
        return 0
    visited.add(pos)

    size = 1
    size += explore_island(grid, row+1, col, visited)
    size += explore_island(grid, row-1, col, visited)
    size += explore_island(grid, row, col-1, visited)
    size += explore_island(grid, row, col+1, visited)

    return size

print(find_minimum_island_size(minimum_island_size_data))