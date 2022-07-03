from queue import Queue
from data import has_path_graph_data

def has_path_using_dfs(graph, src, dest, visited=set()):
    visited.add(src)
    if src == dest:
        return True
    for child in graph[src]:
        if child not in visited:
            if has_path_using_dfs(graph, child, dest):
                return True
    return False


def has_path_using_bfs(graph, src, dest, visited=set()):
    queue = Queue()
    queue.put(src)
    while not queue.empty():
        current_node = queue.get()
        if current_node == dest:
            return True
        for child in graph[current_node]:
            if child not in visited:
                queue.put(child)
                visited.add(child)
    return False

src, dest = 'f', 'g'
print(has_path_using_dfs(has_path_graph_data, src, dest))
print(has_path_using_bfs(has_path_graph_data, src, dest))
