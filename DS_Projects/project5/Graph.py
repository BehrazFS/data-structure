import math
from ArrayList import ArrayList
from Matrix import Matrix
from HashMap import HashMap
from Stack import Stack


class Vertex:
    def __init__(self, index, data=None):
        self.index = index
        self.data = data

    def __repr__(self):
        return f"{type(self).__name__}({self.index!r}, {self.data!r})"

    def __str__(self):
        return f"{type(self).__name__}({self.index!r}, {self.data!r})"

    def __lt__(self, other):
        return self.data < other

    def __le__(self, other):
        return self.data <= other

    def __gt__(self, other):
        return self.data > other

    def __ge__(self, other):
        return self.data >= other

    def __eq__(self, other):
        return self.data == other.data and self.index == other.index

    def __ne__(self, other):
        return self.data != other.data or self.index != other.index


class Edge:
    def __init__(self, source: Vertex, destination: Vertex, weight=1):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __str__(self):
        return f"{type(self).__name__}: {self.source!r} =={self.weight!r}==>> {self.destination!r}"

    def __repr__(self):
        return f"{type(self).__name__}: {self.source!r} =={self.weight!r}==>> {self.destination!r}"

    def __lt__(self, other):
        return self.weight < other

    def __le__(self, other):
        return self.weight <= other

    def __gt__(self, other):
        return self.weight > other

    def __ge__(self, other):
        return self.weight >= other

    def __eq__(self, other):
        return self.weight == other.weight and self.source == other.source and self.destination == other.destination

    def __ne__(self, other):
        return self.weight != other.weight or self.source != other.source or self.destination != other.destination


class Graph:
    def __init__(self):
        self.vertices = ArrayList()
        self.edges = ArrayList()
        self.adjacency_list = ArrayList()
        self.adjacency_matrix = Matrix(0, 0)
        self.Time = 0

    def add_vertex(self, data=None):
        new_ver = Vertex(self.vertices.filled, data)
        self.vertices.add(new_ver)
        self.adjacency_list.add(ArrayList())
        self.adjacency_matrix.add_row(math.inf)
        self.adjacency_matrix.add_column(math.inf)

    def add_edge(self, source: Vertex, destination: Vertex, weight=1):
        new_edge = Edge(source, destination, weight)
        self.edges.add(new_edge)
        self.adjacency_list[source.index].add([destination, weight])
        self.adjacency_matrix[source.index][destination.index] = weight

    def add_edge_two_way(self, source: Vertex, destination: Vertex, weight=1):
        self.add_edge(source, destination, weight)
        self.add_edge(destination, source, weight)

    def remove_edge_two_way(self, source: Vertex, destination: Vertex, weight=1):
        self.remove_edge(source, destination, weight)
        self.remove_edge(destination, source, weight)

    def remove_edge(self, source: Vertex, destination: Vertex, weight=1):
        removing_edge = Edge(source, destination, weight)
        self.edges.remove(removing_edge)
        self.adjacency_list[source.index].remove([destination, weight])
        self.adjacency_matrix[source.index][destination.index] = math.inf

    def update_edge_weight(self, source: Vertex, destination: Vertex, new_weight=1):
        for i in self.edges:
            if i.source == source and i.destination == destination:
                i.weight = new_weight
        for i in self.adjacency_list[source.index]:
            if i[0] == destination:
                i[1] = new_weight
        self.adjacency_matrix[source.index][destination.index] = new_weight

    def get_edge_weight(self, source: Vertex, destination: Vertex):
        return self.adjacency_matrix[source.index][destination.index]

    def __contains__(self, item):
        ans = False
        for i in self.vertices:
            if (i is not None) and (item == i.data):
                ans = True
                break
        return ans

    def __setitem__(self, key, value):
        self.vertices[key].data = value

    def __getitem__(self, item):
        return self.vertices[item]

    def __len__(self):
        return self.vertices.filled

    def __iter__(self):
        for i in self.vertices:
            yield i

    def get(self, data):
        for i in self.vertices:
            if i.data == data:
                return i

    def get_Floyd_warshall(self):
        weghts = [[[math.inf for i in range(len(self))] for i in range(len(self))] for i in range(len(self))]
        for k in range(len(self)):
            for i in range(len(self)):
                for j in range(len(self)):
                    if k == 0:
                        weghts[k][i][j] = self.adjacency_matrix[i][j]
                    else:
                        weghts[k][i][j] = min(weghts[k - 1][i][j], weghts[0][i][k] + weghts[k - 1][k][j],
                                              weghts[k - 1][i][k] + weghts[0][k][j])
        return weghts


# g = Graph()
# print(g.adjacency_matrix)
# print(g.adjacency_list)
# print(g.vertices)
# print(g.edges)
# g.add_vertex(10)
# g.add_vertex(20)
# g.add_vertex(30)
# g.add_vertex("d")
# print(g.adjacency_matrix)
# print(g.adjacency_list)
# print(g.vertices)
# print(g.edges)
# g.add_edge(g.vertices[0], g.vertices[2], 10)
# g.add_edge(g.vertices[0], g.vertices[1], 12)
# g.add_edge(g.vertices[2], g.vertices[1])
# g.add_edge(g.vertices[1], g.vertices[1], 170)
# print(g.adjacency_matrix)
# print(g.adjacency_list)
# print(g.vertices)
# print(g.edges)
# # g.remove_edge(g.vertices[0], g.vertices[2], 10)
# # g.remove_edge(g.vertices[0], g.vertices[1], 12)
# # g.remove_edge(g.vertices[2], g.vertices[1])
# g.remove_edge(g.vertices[1], g.vertices[1], 170)
# g.add_vertex("gh")
# g[1] = 444
# print(g.adjacency_matrix)
# print(g.adjacency_list)
# print(g.vertices)
# print(g.edges)
# print("ghs" in g)
# print(len(g))
# for v in g:
#     print(v)
# g.update_edge_weight(g.vertices[0], g.vertices[2], 1000)
# print(g.adjacency_matrix)
# print(g.adjacency_list)
# print(g.vertices)
# print(g.edges)

class IntegerGraph:

    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = ArrayList()
        for i in range(self.V):
            self.graph.add(ArrayList())
        self.Time = 0

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].add(v)

    def removeEdge(self, u, v):
        self.graph[u].remove(v)

    def addVertex(self, num: int):
        for i in range(num):
            self.V += 1
            self.graph.add(ArrayList())

    '''A recursive function that find finds and prints strongly connected
    components using DFS traversal
    u --> The vertex to be visited next
    disc[] --> Stores discovery times of visited vertices
    low[] -- >> earliest visited vertex (the vertex with minimum
                discovery time) that can be reached from subtree
                rooted with current vertex
     st -- >> To store all the connected ancestors (could be part
           of SCC)
     stackMember[] --> bit/index array for faster check whether
                  a node is in stack
    '''

    def SCCUtil(self, u, low, disc, stackMember, st, g: Graph = None):

        # Initialize discovery time and low value
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        stackMember[u] = True
        st.push(u)

        # Go through all vertices adjacent to this
        for v in self.graph[u]:

            # If v is not visited yet, then recur for it
            if disc[v] == -1:

                self.SCCUtil(v, low, disc, stackMember, st,g)

                # Check if the subtree rooted with v has a connection to
                # one of the ancestors of u
                # Case 1 (per above discussion on Disc and Low value)
                low[u] = min(low[u], low[v])

            elif stackMember[v] == True:

                '''Update low value of 'u' only if 'v' is still in stack
                (i.e. it's a back edge, not cross edge).
                Case 2 (per above discussion on Disc and Low value) '''
                low[u] = min(low[u], disc[v])

        # head node found, pop the stack and print an SCC
        w = -1  # To store stack extracted vertices
        if low[u] == disc[u]:
            while w != u:
                w = st.pop()
                if g is None:
                    print(w, end=" ")
                else:
                    print(g[w].data, end=" , ")
                stackMember[w] = False

            print()

    # The function to do DFS traversal.
    # It uses recursive SCCUtil()

    def SCC(self, g: Graph = None):

        # Mark all the vertices as not visited
        # and Initialize parent and visited,
        # and ap(articulation point) arrays
        disc = [-1] * (self.V)
        low = [-1] * (self.V)
        stackMember = [False] * (self.V)
        st = Stack()

        # Call the recursive helper function
        # to find articulation points
        # in DFS tree rooted with vertex 'i'
        for i in range(self.V):
            if disc[i] == -1:
                self.SCCUtil(i, low, disc, stackMember, st, g)

# g1 = IntegerGraph(5)
# g1.addEdge(1, 0)
# g1.addEdge(0, 2)
# g1.addEdge(2, 1)
# g1.addEdge(0, 3)
# g1.addEdge(3, 4)
# print("SSC in first graph ")
# g1.SCC()
#
# g2 = IntegerGraph(4)
# g2.addEdge(0, 1)
# g2.addEdge(1, 2)
# g2.addEdge(2, 3)
# print("\nSSC in second graph ")
# g2.SCC()

# g3 = IntegerGraph(7)
# g3.addEdge(0, 1)
# g3.addEdge(1, 2)
# g3.addEdge(2, 0)
# g3.addEdge(1, 3)
# g3.addEdge(1, 4)
# g3.addEdge(1, 6)
# g3.addEdge(3, 5)
# g3.addEdge(4, 5)
# print("\nSSC in third graph ")
# g3.SCC()

# g4 = IntegerGraph(5)
# g4.addEdge(0, 1)
# g4.addEdge(0, 3)
# g4.addEdge(1, 2)
# g4.addEdge(1, 4)
# g4.addEdge(2, 0)
# g4.addVertex(6)
# g4.addEdge(2, 6)
# g4.addEdge(3, 2)
# g4.addEdge(4, 5)
# g4.addEdge(4, 6)
# g4.addEdge(5, 6)
# g4.addEdge(5, 7)
# g4.addEdge(5, 8)
# g4.addEdge(5, 9)
# g4.addEdge(6, 4)
# g4.addEdge(7, 9)
# g4.addEdge(8, 9)
# g4.addEdge(9, 8)
# print("\nSSC in fourth graph ")
# g4.SCC()

# g5 = IntegerGraph(5)
# g5.addEdge(0, 1)
# g5.addEdge(1, 2)
# g5.addEdge(2, 3)
# g5.addEdge(2, 4)
# g5.addEdge(3, 0)
# g5.addEdge(4, 2)
# print("\nSSC in fifth graph ")
# g5.SCC()
