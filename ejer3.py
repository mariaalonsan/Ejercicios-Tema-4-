class Vertex:
    def __init__(self, name, v_type):
        self.name = name
        self.v_type = v_type
        self.adjacent = {}

    def add_neighbor(self, neighbor, weight=1):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def __str__(self):
        return f"{self.name}: {self.adjacent}"


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def add_vertex(self, name, v_type):
        self.num_vertices += 1
        new_vertex = Vertex(name, v_type)
        self.vert_dict[name] = new_vertex
        return new_vertex

    def add_edge(self, frm, to, weight=1):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)
        self.vert_dict[frm].add_neighbor(self.vert_dict[to], weight)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], weight)

    def dijkstra(self, start, target):
        import heapq

        dist = {vertex: float('infinity') for vertex in self.vert_dict}
        dist[start] = 0

        pq = [(0, start)]

        while pq:
            cur_dist, cur_vertex = heapq.heappop(pq)

            if cur_dist > dist[cur_vertex]:
                continue

            for neighbor, weight in self.vert_dict[cur_vertex].adjacent.items():
                distance = cur_dist + weight

                if distance < dist[neighbor.name]:
                    dist[neighbor.name] = distance
                    heapq.heappush(pq, (distance, neighbor.name))

        return dist[target]

# Creación del grafo y de sus vértices
g = Graph()

stations = ["King's Cross", "Waterloo", "Victoria Train Station", "Liverpool Street Station", "St. Pancras", "Paddington"]
junctions = [str(i) for i in range(1, 13)]

for station in stations:
    g.add_vertex(station, 'station')

for junction in junctions:
    g.add_vertex(junction, 'junction')

# Conexiones entre los vértices
g.add_edge("King's Cross", '1')
g.add_edge('1', '2')
g.add_edge('2', '3')
g.add_edge('3', 'Waterloo')
g.add_edge('Victoria Train Station', '4')
g.add_edge('4', '5')
g.add_edge('5', '6')
g.add_edge('6', 'Liverpool Street Station')
g.add_edge('St. Pancras', '7')
g.add_edge('7', '8')
g.add_edge('8', "King's Cross")

# Encuentra el camino más corto
print("Camino más corto de King's Cross a Waterloo:", g.dijkstra("King's Cross", 'Waterloo'))
print("Camino más corto de Victoria Train Station a Liverpool Street Station:", g.dijkstra('Victoria Train Station', 'Liverpool Street Station'))
print("Camino más corto de St. Pancras a King's Cross:", g.dijkstra('St. Pancras', "King's Cross"))
