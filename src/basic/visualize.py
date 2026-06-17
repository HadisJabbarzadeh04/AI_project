from basic.search_result import print_result

import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(graph, path=None):

    G = nx.DiGraph()

    for node, neighbors in graph.graph.items():
        for neighbor, cost in neighbors:
            G.add_edge(node, neighbor, weight=cost)

    pos = nx.spring_layout(G)

    plt.figure(figsize=(8, 6))

    nx.draw(
        G, pos,
        with_labels=True,
        node_color='lightblue',
        node_size=2000,
        font_size=12,
        edge_color='gray'
    )

    labels = nx.get_edge_attributes(G, 'weight')

    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    if path:
        edges = list(zip(path, path[1:]))

        nx.draw_networkx_edges(
            G, pos,
            edgelist=edges,
            edge_color='red',
            width=3
        )

    plt.title("Search Result")
    plt.show()




