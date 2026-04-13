def dijkstra(graph, start):

    # distances (tentative)
    dist = {}
    # previous router (to rebuild path)
    prev = {}
    # visited routers (fixed)
    visited = []

    # initialization
    for node in graph:
        dist[node] = float("inf")
        prev[node] = None

    dist[start] = 0

    # list of nodes to process (the "file")
    nodes = list(graph.keys())

    while nodes:

        # 1) find the node with the smallest distance
        min_node = None
        for node in nodes:
            if min_node is None or dist[node] < dist[min_node]:
                min_node = node

        # remove it from the file
        nodes.remove(min_node)
        visited.append(min_node)

        # 2) update neighbors
        for neighbor in graph[min_node]:

            cost = graph[min_node][neighbor]
            new_distance = dist[min_node] + cost

            # relaxation step
            if new_distance < dist[neighbor]:
                dist[neighbor] = new_distance
                prev[neighbor] = min_node

    return dist, prev

# rebuild shortest path
def get_path(prev, start, end):
    path = []
    node = end

    while node is not None:
        path.append(node)
        node = prev[node]

    path.reverse()
    return path

# test it
dist, prev = dijkstra('graph', "A")

print("Distances:", dist)
print("Path A -> B:", get_path(prev, "A", "B"))
print("Path A -> D:", get_path(prev, "A", "D"))
