!pip install igraph -q
import igraph as ig

g = ig.Graph()

g.add_vertices(4)

g.add_edges([
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 3)
])

print("Number of vertices:", g.vcount())
print("Number of edges:", g.ecount())
print("Degree of vertices:", g.degree())