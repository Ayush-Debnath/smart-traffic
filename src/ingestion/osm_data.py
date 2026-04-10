import osmnx as ox

def download_road_network(city: str):
    print(f"[INFO] Downloading road network for {city}...")
    
    graph = ox.graph_from_place(city, network_type='drive')
    
    return graph