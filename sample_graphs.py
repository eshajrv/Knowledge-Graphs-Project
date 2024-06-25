#%%
import networkx as nx

# %%
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import scipy as sp

# Load the CSV file
csv_file = '/Users/eshav/Downloads/curated_Disgenet.csv' 
df = pd.read_csv(csv_file, delimiter=';')

# Select only the relevant columns
edges_df = df[(df['score'] > 0.7) & (df['DSI'] > 0.5)]

# Create an empty graph
G = nx.Graph()

# Add edges to the graph
for index, row in edges_df.iterrows():
    G.add_edge(row['geneId'], row['score'])

layouts = [nx.spring_layout, nx.shell_layout, nx.circular_layout]

# Draw the graph
plt.figure(figsize=(15, 5))
for i, layout in enumerate(layouts):
    plt.subplot(1, 3, i + 1)
    pos = layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=200, font_size=10)
    plt.title(layout.__name__)

plt.tight_layout()
plt.show()

# %%
G= nx.karate_club_graph()
karate_pos = nx.spring_layout(G, k=0.3)
nx.draw_networkx(G, karate_pos)

# %%
#adding the member club attribute to the nodes to split into the 2 clubs 
member_club=[0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
    0, 0, 0, 0, 1, 1, 0, 0, 1, 0,
    1, 0, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1]

for node_id in G.nodes:
    G.nodes[node_id]["club"]= member_club[node_id]

node_colors = ['#1f78b4' if G.nodes[v]["club"]==0
else '#33a02c' for v in G]

nx.draw_networkx(G, karate_pos, label = True, node_color = node_colors)

# %%
#adding attributes to the edges
for v,w in G.edges:
    if G.nodes[v]["club"] == G.nodes[w]["club"]:
        G.edges[v,w]["internal"] = True
    else:
        G.edges[v,w]["internal"] = False

internal = [e for e in G.edges if G.edges[e]["internal"]]
external = [e for e in G.edges if ~G.edges[e]["internal"]]

nx.draw_networkx_nodes(G, karate_pos, node_color=node_colors)
nx.draw_networkx_labels(G, karate_pos)

nx.draw_networkx_edges(G, karate_pos, edgelist=internal)
nx.draw_networkx_edges(G, karate_pos, edgelist=external, style="dashed")

#%%
node_color = [
    '#1f78b4' if G.nodes[v]["club"] == 0
    else '#33a02c' for v in G]
# %%
#adding edge weights 
#tie strength increases when the number of neighbors that have two nodes in common increases
#use the built in neighbors function to find the number of neighbors 
def tie_strength(G, v, w):
    v_neighbors = set(G.neighbors(v))
    w_neighbors = set(G.neighbors(w))
    #return the size of the set intersection
    return 1 + len(v_neighbors & w_neighbors)
    #adding one because a weight of zero would normally mean no edge, so without the 1, edges between nodes without common neighbors wouldnt count as edges
    #in networkx, any edge attribute can be used as a weight

for v,w in G.edges:
    G.edges[v,w]["weight"] = tie_strength(G,v,w)
    #store the weights in a list 

edge_weights = [G.edges[v,w]["weight"] for v, w in G.edges]

#use a spring layout to effectively show the weights
weighted_pos = nx.spring_layout(G, pos=karate_pos, k=0.3, weight="weight")

# Draw network with edge color determined by weight
nx.draw_networkx(
    G, weighted_pos, width=4, node_color=node_color,
    edge_color=edge_weights, edge_vmin=0, edge_vmax=6, edge_cmap=plt.cm.Blues)
# Draw solid/dashed lines on top of internal/external edges
nx.draw_networkx_edges(G, weighted_pos, edgelist=internal, edge_color="gray")
nx.draw_networkx_edges(G, weighted_pos, edgelist=external, edge_color="gray", style="dashed")

# %%
G = nx.read_gexf("/Users/eshav/Downloads/klas12b-net-1.gexf", node_type=int)
student_pos = nx.spring_layout(G, k=1.5)
nx.draw_networkx(G, student_pos, arrowsize=20)

# %%

# Create a new graph
G = nx.Graph()

# Add edges with labels
G.add_edge('A', 'B', age=4)
G.add_edge('A', 'C', age=1)
G.add_edge('B', 'C', age=3)
G.add_edge('B', 'D', age=2)
G.add_edge('C', 'D', age=5)

# Get positions for the nodes in the graph
pos = nx.spring_layout(G)

# Draw the nodes and edges
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')

# Extract edge labels
edge_labels = nx.get_edge_attributes(G, 'age')

# Draw the edge labels
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Show the plot
plt.show()
