#!/usr/bin/env python

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

branching_factor = 4
tree_height = 3
number_of_nodes = branching_factor ** tree_height

fig = plt.figure(1)
ax = fig.add_subplot(3, 1, 1)
graph = nx.star_graph(number_of_nodes)
pos = nx.spring_layout(graph)
pos = nx.graphviz_layout(graph, prog='twopi', args='')
nx.draw(graph, pos, with_labels=False)

ax = fig.add_subplot(3, 1, 2)
graph = nx.balanced_tree(branching_factor, tree_height)
tree_edges = len(graph.edges())
pos = nx.graphviz_layout(graph, prog='twopi', args='')
tree_degrees = nx.degree(graph)
nx.draw(graph, pos, with_labels=False)

ax = fig.add_subplot(3, 1, 3)
degrees = tree_degrees.values()
np.random.shuffle(degrees)
graph = nx.barabasi_albert_graph(number_of_nodes, 2,
                                 seed=222)
graph = graph.to_undirected()
pos = nx.spring_layout(graph, k=0.12, iterations=500)
nx.draw(graph, pos, with_labels=False)

plt.show()
