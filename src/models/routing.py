import osmnx as ox
import networkx as nx
city = "Chandigarh, India"
# graph = ox.graph_from_place(city, network_type="drive")

graph = ox.load_graphml("C:\\Users\\Ayush\\OneDrive\\Desktop\\smart-traffic\\notebooks\\chandigarh.graphml")

origin = (30.7333, 76.7794)   # Sector 17 Plaza (main market + offices)
destination = (30.7046, 76.7179)   # Chandigarh Railway Station

orig_node = ox.distance.nearest_nodes(graph, origin[1], origin[0])
dest_node = ox.distance.nearest_nodes(graph, destination[1], destination[0])

route = nx.shortest_path(graph, orig_node, dest_node, weight='length')

for u, v, k, data in graph.edges(keys=True, data=True):
    base_length = data.get('length', 1)

    # Simulated traffic factor (replace later with real mapping)
    traffic_factor = 1.2  

    data['traffic_weight'] = base_length * traffic_factor

route_traffic = nx.shortest_path(
    graph, orig_node, dest_node, weight='traffic_weight'
)

for u, v, k, data in graph.edges(keys=True, data=True):
    risk_factor = 1.1  # simulate

    data['risk_weight'] = data.get('length', 1) * risk_factor

for u, v, k, data in graph.edges(keys=True, data=True):
    data['final_weight'] = (
        data.get('traffic_weight', 1) * 0.6 +
        data.get('risk_weight', 1) * 0.4
    )

route_final = nx.shortest_path(
    graph, orig_node, dest_node, weight='final_weight'
)

ox.plot_graph_routes(
    graph,
    [route, route_traffic, route_final],
    route_colors=['blue', 'red', 'green']
)