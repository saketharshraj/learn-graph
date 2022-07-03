from queue import Queue
from data import graph_data

def bfs_using_loop(graph, node):
    queue = Queue()
    queue.put(node)
    visited = set()
    while not queue.empty():
        current_node = queue.get()
        print(current_node, '->', end='')
        for child in graph[current_node]:
            if child not in visited:
                queue.put(child)
                visited.add(child)


# BFS using recursion doesn't make any sense since we are using a queue.
def bfs_using_recursion(graph, q: Queue, visited=set()):
    if q.empty():
        return
    current_node = q.get()
    print(current_node, '->', end='')
    for child in graph[current_node]:
        if child not in visited:
            q.put(child)
            visited.add(child)
    bfs_using_recursion(graph, q)



x = Queue()
x.put('a')
bfs_using_loop(graph_data, 'a')
print('\n')
bfs_using_recursion(graph_data, x)