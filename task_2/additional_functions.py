import math


def move_point(point, center, distance):
    """
    function moving point (x, y) from center (center_x, center_y)
    to a given distance
    """
    x, y = point
    center_x, center_y = center

    # calculation of a vector from the center point to a given point
    vector_x = x - center_x
    vector_y = y - center_y

    # vector normalization
    length = math.sqrt(vector_x ** 2 + vector_y ** 2)
    normalized_x = vector_x / length
    normalized_y = vector_y / length

    # move a point to a given distance
    new_x = x + normalized_x * distance
    new_y = y + normalized_y * distance

    return new_x, new_y


def build_complement_graph(adjacency_dict):
    """
    function createg completment graph for given graph
    adjacency_dict should be dict like {'A':['B'], 'B':['A'], 'C':[]}
    """
    
    complement_graph = {}
    
    for vertex in adjacency_dict:
        complement_graph[vertex] = []

    for vertex, neighbors in adjacency_dict.items():
        for other_vertex in adjacency_dict:
            if vertex != other_vertex and other_vertex not in neighbors:
                complement_graph[vertex].append(other_vertex)
    
    return complement_graph
