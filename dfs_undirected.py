from tkinter.font import families
from data import undirected_graph_data

def dfs_using_recursion(graph, node, visited=set()):
    visited.add(node)
    count = 0
    print(node, '->', end='')
    for child in graph[node]:
        if child not in visited:
            count += dfs_using_recursion(graph, child, visited)  # passing visited here has zero effect since visited will automatically have memory of visited nodes reference in recursive call
    count += 1

graph = {}
nodes = undirected_graph_data['nodes']
edges = undirected_graph_data['edges']
for node in nodes:
    graph[node] = set()

for (u, v) in edges:
    graph[u].add(v)
    graph[v].add(u) 

visited = set()
families = []

for child in nodes:
    if child not in visited:
        current_node_family = dfs_using_recursion(graph, child, visited)
        families.append(current_node_family)
        print()