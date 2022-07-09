from data import directed_acyclic_graph_data


def dfs(graph, node, visited, topological_order):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, topological_order)
    topological_order.append(node)

def topological_sort_dfs(graph):
    nodes = graph.keys()
    """
    Given a graph, return a list of nodes in topological order.
    This implementation uses depth-first search.
    """
    # Create a list of nodes in topological order
    topological_order = []
    # Keep track of visited nodes
    visited = set()
    for node in nodes:
        if node not in visited:
            dfs(graph, node, visited, topological_order)
    topological_order.reverse()
    return topological_order

def topological_sort_bfs(graph)

if __name__ == '__main__':
    print(topological_sort_dfs(directed_acyclic_graph_data))
    