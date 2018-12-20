"""Solution to 4.1: Route Between Nodes.

BFS Algorithm:
http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/11-Graph/bfs.html
"""

from queue import Queue


def is_route(dir_graph: list, nodes: tuple):
    """Determine if nodes have a path in graph.

    checks to see if there is a path between two
    nodes in a direct graph via a breadth-first
    search algorithm.

    Args:
        dir_graph: an adjacency list of a directed
        graph.
        nodes: start and end node in a tuple to test
        for pathing.

    Return 
        a boolean value depending on whether or not the 
        nodes given for the graph have a route.
    """
    to_visit = Queue()
    to_visit.put(nodes[0])
    visited = []

    while not to_visit.empty():
        current = to_visit.get()
        if not current in visited:
            visited.append(0)
            for node in dir_graph[current]:
                if node == nodes[1]:
                    return True
                if not node in visited:
                    to_visit.put(node)
    return False
            