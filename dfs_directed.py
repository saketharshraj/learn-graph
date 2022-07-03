from data import directed_graph_data

def dfs_using_loop(graph, node):
    stack = [node]
    visited = set()
    while stack:
        current_node = stack.pop()
        print(current_node, '->', end='')
        for child in graph[current_node]:
            if child not in visited:
                stack.append(child)
                visited.add(child)


def dfs_using_recursion(graph, node, visited=set()):
    visited.add(node)
    print(visited)
    # print(node, '->', end=' ')
    for child in graph[node]:
        if child not in visited:
            dfs_using_recursion(graph, child, visited)  # passing visited here has zero effect since visited will automatically have memory of visited nodes reference in recursive call

dfs_using_loop(directed_graph_data, 'a')
print('\n')
dfs_using_recursion(directed_graph_data, 'a')