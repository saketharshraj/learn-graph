from data import largest_component_graph_data

def largest_component(graph):
    longest = 0
    visited = set()
    for node in graph:
        size = explore_size(graph, node, visited)
        longest = max(longest, size)
    return longest

def explore_size(graph, node, visited):
    if node in visited:
        return 0
    visited.add(node)
    size = 1
    for child in graph[node]:
        size += explore_size(graph, child, visited)
    return size


print(largest_component(largest_component_graph_data))


