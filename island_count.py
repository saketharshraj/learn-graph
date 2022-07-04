from data import island_grid_data

def island_count(grid):
    visited = set()
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            count += explore_island(grid, row, col, visited) == True
    return count

def explore_island(grid, row, col, visited):
    row_bound = 0 <= row < len(grid)
    col_bound = 0 <= col < len(grid[0])
    if not row_bound or not col_bound:
        return False

    if (grid[row][col] == 'W'):
        return False
    pos = f'{row},{col}'
    if pos in visited:
        return False
    visited.add(pos)
    explore_island(grid, row-1, col, visited)
    explore_island(grid, row+1, col, visited)
    explore_island(grid, row, col-1, visited)
    explore_island(grid, row, col+1, visited)

    return True

print(island_count(island_grid_data))