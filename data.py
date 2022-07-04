directed_graph_data = {
    'a': ['b', 'c'],
    'b': ['c', 'd'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
}

has_path_graph_data = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': [],
}

undirected_graph_data = {
    'edges': [['i', 'j'], ['k', 'i'], ['m', 'k'], ['k', 'l'], ['o', 'n']],
    'nodes': ['i', 'j', 'k', 'l', 'm', 'n', 'o' ],
}

largest_component_graph_data = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}

shortest_path_graph_data = {
    'edges' : [[1,2], [2,3], [3,4], [4,5], [5,6], [6,1]],
    'nodes' : [x for x in range(1, 7)]
}

island_grid_data = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]

minimum_island_size_data = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]