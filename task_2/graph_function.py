import math
import random

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import additional_functions


class Graph:

    def __init__(self):
        self.nodes = {}
        self.edges = []
        self.pictures = False
        self.circle = (6, 6, 4)

    def add_node(self, node_id, node_info, x='no_info', y='no_info'):
        if node_id in self.nodes.keys():
            raise ValueError("Node with the same id already exists.")
        else:
            self.nodes[node_id] = {'info': node_info, 'x': x, 'y': y}

    def add_edge(self, node_id1, node_id2):
        if node_id1 in self.nodes and node_id2 in self.nodes:
            self.edges.append([node_id1, node_id2])
        else:
            raise ValueError("One or both of the nodes do not exist.")

    def generate_random_graph(self, num_nodes, num_edges):
        x0, y0, r = self.circle 
        
        if num_edges > num_nodes * (num_nodes - 1) / 2:
            raise ValueError("The number of edges is greater than possible.")
        else:
            grad = 0
            # create random unique nodes
            for i in range(num_nodes):
                node_id = str(i)
                node_info = "Node " + str(i)

                x = round(r * math.cos(-(grad - 90) * (math.pi / 180)) + x0, 2)
                y = round(r * math.sin(-(grad - 90) * (math.pi / 180)) + y0, 2)
                grad += 360 / num_nodes

                self.add_node(node_id, node_info, x, y)

            nodes_list = list(self.nodes.keys())
            temp_nodes = {k: [] for k in nodes_list}

            # create random unique edges
            for _ in range(num_edges):
                possible_nodes_1 = [k for k, v in temp_nodes.items() if len(v) < len(temp_nodes) - 1]
                node_id1 = random.choice(possible_nodes_1)

                possible_nodes_2 = [k for k, v in temp_nodes.items() if node_id1 not in v and k != node_id1]
                node_id2 = random.choice(possible_nodes_2)

                temp_nodes[node_id1].append(node_id2)
                temp_nodes[node_id2].append(node_id1)

                self.add_edge(node_id1, node_id2)

    def draw_graph(self, x_max=12, y_max=12, show_clique=None):
        if show_clique is None:
            show_clique = list(self.nodes.keys())
        else:
            pass
        
        x0, y0, r = self.circle 
        g = plt.figure()
        ax = g.add_subplot(111)
        if not self.pictures:
            distance = 1.4
        else:
            distance = 2
        grad = 0
        num_nodes = len(self.nodes)

        # fill missing coordintaes
        for key in self.nodes.keys():
            if self.nodes[key]['x'] == 'no_info':
                self.nodes[key]['x'] = round(r * math.cos(-(grad - 90) * (math.pi / 180)) + x0, 2)
                self.nodes[key]['y'] = round(r * math.sin(-(grad - 90) * (math.pi / 180)) + y0, 2)
            grad += 360 / num_nodes

        # print edges
        for edge in self.edges:
            if edge[0] in show_clique and edge[1] in show_clique:
                x = [self.nodes[edge[0]]['x'], self.nodes[edge[1]]['x']]
                y = [self.nodes[edge[0]]['y'], self.nodes[edge[1]]['y']]
                ax.plot(x, y, 'k-')
            else:
                pass

        # print annotation info
        for node_id, node_data in self.nodes.items():
            if node_id in show_clique:
                annotate_x, annotate_y = additional_functions.move_point(point=(node_data['x'], node_data['y']),
                                                                         center=(x0, y0), distance=distance)
                ax.annotate(node_data['info'], (annotate_x, annotate_y), zorder=11,
                            textcoords="offset points", ha='center',  xytext=(0, -10),
                            bbox=dict(boxstyle='round,pad=0.5', fc='white',  alpha=0.5))
            else:
                pass

        # print point or picture of a node
        for key in self.nodes.keys():
            if key in show_clique:
            
                x = self.nodes[key]['x']
                y = self.nodes[key]['y']
            
                if not self.pictures:
                    ax.scatter(x, y, color='black')
                else:
                    img = mpimg.imread(f"image_{key}.png")
                    imgplot = ax.imshow(img, extent=[x-0.8, x+0.8, y-0.8, y+0.8],
                                        zorder=10, aspect='auto')

        ax.set_xlim(0, x_max)
        ax.set_ylim(0, y_max)
        ax.axis('off')
        ax.set_aspect('equal')
        
        plt.show()
        
    def create_adjacency_dict(self):
        adjacency_dict = {k: set() for k in self.nodes.keys()}
        for edge in self.edges:
            adjacency_dict[edge[0]].add(edge[1])
            adjacency_dict[edge[1]].add(edge[0])
        adjacency_dict = {k: list(v) for k, v in adjacency_dict.items()}
        return adjacency_dict
            
