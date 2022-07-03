def build_graph(nodes, edges):
    graph = {}

    for node in nodes:
        graph[node] = set()

    for (u, v) in edges:
        graph[u].add(v)
        graph[v].add(u) 

    return graph