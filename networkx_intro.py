#%%
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edge(1,2)
G.add_edge(2,3)

nx.draw_spring(G, with_labels= True)

plt.show()
# %%
edge_list = [(1,2), (2,3), (3,4), (3,5), (4,6), (6,7)]
G = nx.from_edgelist(edge_list)
nx.draw_circular(G, with_labels= True)
plt.show()

# %%
#Regular undirected Graph with self loops 
G.add_node(1)
G.add_nodes_from([2, 3])

H = nx.path_graph(10)
G.add_nodes_from(H)

G.add_edge(1, 2)

G.add_edges_from([(1, 2), (1, 3)])

G.add_edges_from([(3, 4), (4, 5)], color="red")
G.add_edges_from([(1, 2, {"color": "blue"}), (2, 3, {"weight": 8})])

plt.figure(figsize=(12, 10))
pos = nx.spring_layout(G) 
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=10)

plt.show()

# %%
#Directed Graph with self connected loops
G = nx.DiGraph()

G.add_nodes_from([2, 3])
G.add_nodes_from(range(100, 110))
H = nx.path_graph(10)
G.add_nodes_from(H)

G.add_edges_from([(1, 2), (1, 3)])

G.add_node(1, time="5pm")
G.add_nodes_from([3], time="2pm")
G.nodes[1]
{'time': '5pm'}
G.nodes[1]["room"] = 714
del G.nodes[1]["room"]
list(G.nodes(data=True))
[(1, {'time': '5pm'}), (3, {'time': '2pm'})]

G.add_edge(1, 2, weight=4.7)
G.add_edges_from([(3, 4), (4, 5)], color="red")
G.add_edges_from([(1, 2, {"color": "blue"}), (2, 3, {"weight": 8})])
G[1][2]["weight"] = 4.7
G.edges[1, 2]["weight"] = 4

plt.figure(figsize=(12, 10))
pos = nx.spring_layout(G) 
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=10)

plt.show()

# %%
G = nx.MultiGraph()

G.add_node(1)
G.add_nodes_from([2, 3])

H = nx.path_graph(10)
G.add_nodes_from(H)

G.add_edge(1, 2)

G.add_edges_from([(1, 2), (1, 3)])

G.add_edges_from([(3, 4), (4, 5)], color="red")
G.add_edges_from([(1, 2, {"color": "blue"}), (2, 3, {"weight": 8})])

plt.figure(figsize=(12, 10))
pos = nx.spring_layout(G) 
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=10)

plt.show()

# %%
G = nx.Graph(day="Friday")
G.graph
G.add_node(1, time = '5pm')
G.add_nodes_from([3], time = '2pm')
plt.figure(figsize=(12, 10))
pos = nx.circular_layout(G) 
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=10)

# %%
#adding nodes with attributes
G = nx.Graph()

G.add_node(1, name="Alice", age = 23, job = "Engineer")
G.add_node(2, name="Jon", age = 24, job = "Doctor")
G.add_node(3, name="Ellie", age = 25, job="Lawyer")

G.add_edge(1,2)
G.add_edge(2,3)

pos = nx.spring_layout(G) 

node_labels = nx.get_node_attributes(G, 'name', 'age')
nx.draw(G, pos, with_labels=True, labels=node_labels, node_color='skyblue', node_size=3000, font_size=15)

nx.draw_networkx_edges(G, pos)

plt.show()
# %%
