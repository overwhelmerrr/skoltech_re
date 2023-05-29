def bron_kerbosch_max_by_inclusion(adjacency_dict):
    """
    variation of bron kerbosh method of clique searching
    """
    results = []
    vertices = list(adjacency_dict.keys())
    num_vertices = len(vertices)
    adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    # create adjacency_matrix from adjacency_dict
    for i in range(num_vertices):
        for j in range(num_vertices):
            if vertices[j] in adjacency_dict[vertices[i]]:
                adjacency_matrix[i][j] = 1

    def bron_kerbosch(r, p, x):
        if not p and not x:
            results.append(r)
            return

        for v_index in p[:]:
            v = vertices[v_index]
            neighbors = adjacency_matrix[v_index]
            bron_kerbosch(
                r + [v],
                [vertex_index for vertex_index in p if neighbors[vertex_index]],
                [vertex_index for vertex_index in x if neighbors[vertex_index]]
            )
            p.remove(v_index)
            x.append(v_index)

    bron_kerbosch([], list(range(num_vertices)), [])

    # return clique/s with max size
    max_size = max(len(clique) for clique in results)
    max_cliques = [clique for clique in results if len(clique) == max_size]

    return max_cliques
