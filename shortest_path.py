# For finding the shortest path between two nodes in a graph, bfs id optimal choice.

from build_graph import build_graph
from data import shortest_path_graph_data
from queue import Queue

class Node:
    def __init__(self, value, distance=0):
        self.value = value
        self.distance = distance


def find_shortest_path(graph, node: Node, ending_value, visited=set()):
    queue = Queue()
    visited.add(node.value)
    queue.put(node)
    while not queue.empty():
        current_node = queue.get()
        if current_node.value == ending_value:
            return current_node.distance
        for neighbor in graph[current_node.value]:
            if neighbor not in visited:
                neighbor_node = Node(neighbor, current_node.distance + 1)
                queue.put(neighbor_node)
                visited.add(neighbor)
    return -1


nodes = shortest_path_graph_data['nodes']
edges = shortest_path_graph_data['edges']
graph = build_graph(nodes=nodes, edges=edges)
starting_value = 1
ending_value = 3
starting_node = Node(starting_value)

print(find_shortest_path(graph, starting_node, ending_value))