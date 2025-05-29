import networkx as nx
import matplotlib.pyplot as plt

# Create the full network graph
G = nx.Graph()
nodes = ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10"]
edges = [("P1", "P2"), ("P1", "P3"), ("P2", "P3"), ("P2", "P4"), ("P2", "P5"),
         ("P3", "P6"), ("P4", "P7"), ("P5", "P8"), ("P6", "P9"), ("P8", "P10")]
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Calculate degree for each node
degrees = dict(G.degree())

# Assign colors based on degree
color_map = []
for node in nodes:
    degree = degrees[node]
    if degree == 4:
        color_map.append('red')
    elif degree == 3:
        color_map.append('orange')
    elif degree == 2:
        color_map.append('blue')
    else:
        color_map.append('green')

# Store colors in a dictionary for consistency
color_dict = dict(zip(nodes, color_map))

# Draw the full network graph
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color=color_map, node_size=500, font_size=12)
plt.title("Full Friendship Network")
plt.savefig("friendship_network.png")
plt.close()

# Create and draw the clique subgraph (P1, P2, P3)
G_clique = nx.Graph()
clique_nodes = ["P1", "P2", "P3"]
clique_edges = [("P1", "P2"), ("P1", "P3"), ("P2", "P3")]
G_clique.add_nodes_from(clique_nodes)
G_clique.add_edges_from(clique_edges)

# Use the same colors as the full network
clique_color_map = [color_dict[node] for node in clique_nodes]

plt.figure(figsize=(6, 4))
pos_clique = nx.circular_layout(G_clique)
nx.draw(G_clique, pos_clique, with_labels=True, node_color=clique_color_map, node_size=500, font_size=12)
plt.title("P1-P2-P3 Clique")
plt.savefig("clique_subgraph.png")
plt.close()

print("Graphs generated: 'friendship_network.png' and 'clique_subgraph.png'")