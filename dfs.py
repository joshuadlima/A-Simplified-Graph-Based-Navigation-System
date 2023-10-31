from collections import deque
from input import *
from main import *
from plotting_resources import *


class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def dfs(self, node, visited):
        if node not in visited:
            # print(node)
            global prev_node
            if node != prev_node:
                lines.append(
                    returnline(
                        name_to_longlat[prev_node],
                        name_to_longlat[node],
                    )
                )

            visited.add(node)
            for neighbor, _ in self.get_neighbors(node):
                prev_node = node
                self.dfs(neighbor, visited)

    def dfs_traversal(self, start_node):
        visited = set()
        print("DFS Traversal:")
        self.dfs(start_node, visited)


graph = Graph(adjacency_list)
start_node = "mapusa"
prev_node = "mapusa"
graph.dfs_traversal(start_node)


# print(lines)
# update index
features = [
    {
        "type": "Feature",
        "geometry": {
            "type": "LineString",
            "coordinates": line["coordinates"],
        },
        "properties": {
            "times": line["dates"],
            "style": {
                "color": line["color"],
                "weight": line["weight"] if "weight" in line else 5,
            },
        },
    }
    for line in lines
]

# Lon, Lat order.

folium.plugins.TimestampedGeoJson(
    {
        "type": "FeatureCollection",
        "features": features,
    },
    period="PT1M",
    add_last_point=True,
).add_to(m)
m.save("index.html")

import webbrowser
webbrowser.open("index.html")
