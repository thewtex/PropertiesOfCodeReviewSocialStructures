#!/usr/bin/env python

import os
import json
import networkx as nx
from networkx.readwrite import json_graph

current_dir = os.path.dirname(__file__)
with open(os.path.join(current_dir, 'GerritGraph.json'), 'rb') as fp:
    data = json.load(fp)

graph = json_graph.node_link_graph(data)
graph = graph.to_undirected()
betweenness = nx.centrality.betweenness_centrality(graph)
for node, between in betweenness.iteritems():
    graph.node[node]['betweenness'] = between
closeness = nx.centrality.closeness_centrality(graph)
for node, close in closeness.iteritems():
    graph.node[node]['closeness'] = close

data = json_graph.node_link_data(graph)
with open(os.path.join(current_dir, '..', 'figures', 'itk_graph.json'), 'wb') as fp:
    json.dump(data, fp)
