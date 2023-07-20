# self-loop => if its two endpoints coincide
# The degree of a vertex v, denoted deg(v), is the number of incident edges of v.
# A self-llop may occur in a graph associated with 
# 1. path : A path is a sequence of alternating vertices and edges that starts at a vertex and ends at a vertex such that each is incident to its predecessor and successor vertex
# 2. cycle : is a path that starts and ends at the same vertex, and that includes at least one edge.

# path is "simple": 

# endpoints(): Return a tuple (u, v) such that vertex u is the origin of the edge and vertex v is the destination; for un undirected graph, the orientation is arbitrary.
# opposite(v):
# vertex_count() => Return the number of vertices of the graph. 
# remove_vertex(x) => Remove vertex v and all its incident edges from the graph.
# remove_edge(e) => Remove edge e from the graph

# vertex objects associated with the endpoint vertices of e.
# It is worth discussing why the remove_vertex(v)


# 14.4.2 Adjancency List Structure
# The adjacent list structure groups the edges of a graph by storing them in smaller
# Specifically, for each vertex v, we maintain a collection (可重複) I(v), called the "incidence collection" of v
# In the case of a directed graph, outgoing and incoming edges can be respectively stored in two separate collections, Iout(v) and Iin(v)
# This could be done by using a positional list to represent V
# Collection V is the primary list of vertices,
# Return an iteration of all edges incident to vertex v.
# We have already noted that the incident_edges(v) method can be achieved in O(deg(v)) time based on use of I(v)
# We can achieve the degree(v) method of the graph ADT to use O(1) time.
# remove_vertex(v) => O(deg(v))
# The easiest way to support edges() in O(m)
# taking care not to report an undirected edge (u, v) twice.

# We note that array A is symmetric if graph G 
# However, several operation are less efficient with an adjacen
# We also assume that there is a secondary edge list (not pictured), to allow the "edges()" method to run in O(m) time, for a graph with m edges.

# 14.2.5 Python Implementation
# The list V is replaced by a top-level dictionary D that 


class Graph:
    # ------------- nested Vertex class ---------------------
    class Vertex:
        """Lightweight vertex structure for a graph"""
        __slots__ = '_element'

        def __init__(self, x):
            """Do not call constructor directly. Use Graph's insert_vertex(x)"""
            self._element = x
        
        def element(self):
            """Return element associated with this vertex."""
            return self._element
        
        def __hash__(self):                                      # will allow vertex to be a map/set key
            return hash(id(self))
    
    # ------------- nested Edge class ------------------------
    class Edge:
        """Lightweight edge structure for a graph."""
        __slots__ = '_origin', '_destination', '_element'
        
        def __init__(self, u, v, x):
            """Do not call constructor directly. Use Graph's insert_edge(u, v, x)."""
            self._origin = u
            self._destination = v
            self._element = x
        
        def endpoint(self):
            """Return (u, v) tuple for vertices u and v."""
            return (self._origin, self._destination)
        
        def opposite(self, v):
            """Return the vertex that is opposite v on this edge."""
            return self._destination if v is self._origin else self._origin
        
        def element(self):
            """Return element associated with this edge."""
            return self._element
        
        def __hash__(self):                                    # will allow edge to be a map/set key
            return hash((self._origin, self._destination))


    """Representation of a simple graph using an adjacency map."""
    def __init__(self, directed = False):
        """Create an empty graph (undirected, by default).
        Graph is directed if optional parameter is set to True
        """
        self._outgoing = {}
        # only create second map for directed graph; use alias for undirected
        self._incoming = {} if directed else self._outgoing
    
    def is_directed(self):
        """Return True if this is a directed graph; False if undirected. 
        如果是有向圖，return True. 如果是無向圖，return False
        Property is based on the original declaration of the graph, not its contents.
        """
        return self._incoming is not self._outgoing  # directed if maps are distinct
    

    def vertex_count(self):
        """Return the number of vertices in the graph."""
        return len(self._outgoing)
    

    def vertices(self):
        """Return an iteration of all vertices of the graph."""
        return self._outgoing.keys()
    

    def edge_count(self):
        """Return the number of edges in the graph."""
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        # for undirected graphs, make sure not to double-count edges
        return total if self.is_directed() else total // 2
    

    def edges(self):
        """Return a set of all edges of the graph."""
        result = set()                                 # avoid double-reporting edges of undirected graph
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())      # add edges to resulting set
        return result
    

    def get_edge(self, u, v):
        """Return the edge from u to v, or None if not adjacent."""
        return self._outgoing[u].get(v)               # returns None if v not adjacent
    

    def degree(self, v, outgoin = True):
        """Return number of (outgoing) edges incident to vertex v in the graph.
        If graph is directed, optional parameter used to count incoming edges.
        """
        adj = self._outgoing if outgoin else self._incoming
        return len(adj[v])
    

    def incident_edges(self, v, outgoin = True):
        """Return all (outgoing) edges incident to vertex v in the graph.
        
        If graph is directed, optional parameter used to request incoming edges.
        """
        adj = self._outgoing if outgoin else self._incoming
        for edge in adj[v].values():
            yield edge
    

    def insert_vertex(self, x = None):
        """Insert and return a new Vertex with element x."""
        v = self.Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}                     # need distinct map for incoming edges
        print('graph is =>', self.graph())
        return v

    def insert_edge(self, u, v, x = None):
        """Insert and return a new Edge from u to v with auxiliary element x."""
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e
        return self.graph()
    

    def get_vertex(self, v):
        for key in self.vertices():
            if key.element() == v:
                return key
    
    def graph(self):
        return {
            out_key.element():
            {in_key.element(): in_value.element() for in_key, in_value in out_value.items()} 
            for out_key, out_value in self._outgoing.items()
        }
            

# Formally, a traversal is a systematic procedure for 

# Whenever an edge e = (u, v) is used to discover a new vertex v during the DFS algorithm
# When performing a DFS on a directed graph, there are three possible kinds of nontree edges:
# Properties of a Depth-First Search
# Since we only follow a discovery edge when we go to an unvisited vertex, we will never form a cycle with such edges. Therefore
### Let G be a directed graph. 
# Depth-first search on G starting at a vertex "s" visits all the vertices of G

# We prove the second fact by induction on the steps of the algorithm.
# We claim that each time a discoveryedge (u, v) is identified, there exists a directed path from s to v in the DFS tree.
# s => u => v
# Note that since back edges always connect a vertex v to a previously visited vertex u,

# Note that DFS is called at most once on each vertex (since it gets marked as visited), 
# and therefore every edge is examined at most twice for an undirected graph,
# once from each of its end vertices 
# and at most once in a directed graph.
# A graph is connnected if, for any two vertices, there is a path between them.

### 14.3.2 DFS Implementation and Extensions
# We begin by providing a Python implementation of the basic depth-first search algorithm, originally described with pseudo-code in Code 

# A graph is "connected" if, for any two vertices, there is a path between them.
# A directed graph G is "strongly connected" if for any two vertices u and v of G, u reaches v and v reaches u.


def DFS(g, u, discovered):
    """Perform DFS of the undiscovered portion of Graph g starting at Vertex u.
    
    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the DFS. (u should be "discovered" prior to the call.)
    """
    for e in g.incident_edges(u):             # for every outgoing edge from u
        v = e.opposite(u)
        if v not in discovered:               # v is an univisited vertex
            discovered[v] = e                 # e is the tree edge that discovered u
            DFS(g, v, discovered)
    return discovered


def DFS_val(g, u, discovered):
    for e in g.incident_edges(u):
        v = e.opposite(u)
        print('v.element() is =>', v.element())
        if v.element() not in discovered:
            discovered[v.element()] = e.element()
            DFS_val(g, v, discovered)
    return discovered


def construct_path(u, v, discovered):
    path = []
    if v in discovered:
        # we build list from v to u and then reverse it at the end
        path.append(v.element())
        walk = v
        while walk is not u:
            e = discovered[walk]
            parent = e.opposite(walk)
            path.append(parent.element())
            walk = parent
        path.reverse()
    return path


def DFS_complete(g):
    """
    Perform DFS for entire graph and return forest as a dictionary.
    Result maps each vertex v to the edge that was used to discover it.
    (Vertices that are roots of a DFS tree are mapped to None.)
    """
    forest = {}
    for u in g.vertices():
        print('u is =>', u)
        if u.element() not in forest:
            forest[u.element()] = None        # u will be the root of a tree
            DFS_val(g, u, forest)
    return forest

### Detecting Cycles with DFS



### 14.3.3 Breadth-First Search
def BFS(g, s, discovered):
    """Perform BFS on the undiscovered portion of Graph g starting at Vertex s.

    discovered is a dictionary mapping each vertex to the edge that was used to discover it during the BFS (s should be mapped to None prior to the call).
    Newly discovered vertices will be added to the dictionary as a result.
    """
    level = [s]                               # first level in cludes only s
    while len(level) > 0:  
        next_level = []                       # prepare to gather newly found vertices     
        for u in level:
            print('u is =>', u.element())
            for e in g.incident_edges(u):     # for every outgoin edge from u
                v = e.opposite(u)
                if v not in discovered:       # v is an unvisited vertex
                    discovered[v] = e
                    next_level.append(v)
        print('next_level is =>', [i.element() for i in next_level])
        level = next_level
    return discovered

# When discussing DFS, we described a classification of nontree edges being either "back edge", which connect a vertex to one of its ancestors, forward edges, which connect a vertex to one of its descendants, or cross edges, which connect a vertex to another vertex that is neither its ancestor nor its descendant.
# The BFS traversal algorithm has a number of interesting properties, some of which we explore in the proposition that follows.
# Most notably, a path in a breadth-first search tree rooted at vertex s to any other vertex v is guaranteed to be the shortest such path from s to v in terms of the number of edges.
# BFS algorithm can also be implemented using a single FIFO queue to represent the current fringe of the search.
# Starting with the source vertex in the queue, we repreatedly remove the vertex from the front of the queue and insert any of its unvisited neighbors to the back of the queue.

# In comparing the capabilities of DFS and BFS, both can be used to efficiently find the set of vertices that are reachable from a given source and to determine paths to those vertices. 
# For an undirected graph, both algorithms can be used to test connectivity, to identify connected components, or to locate a cycle.

# Also, the actual path from vertex s to vertex v can be reconstructed using the 
# Starting with the source vertex in the queue, we repeatedly remove the vertex from the
# The "transitive closure" of a directed graph G is itself a directed graph G such that the vertices of G are the smaller

# Let G be a directed graph with n vertices and m edges.
# We compute the transitive closure of G in a series of rounds

# We initialize G0 = G. 
# We also arbitrarily number the vertices of G as v1, v2, ..., vn
# We then begin the computation of the rounds, beginning with round 1.
# In a generic round k, we construct directed graph Gk starting with Gk = Gk-1
# Floyd-Warshall algorithm
# We illustrate an example run of the Floyd-Warshall algorithm

from copy import deepcopy


def floyd_warshall(g):
    """Return a new graph that is the transitive closure of g."""
    closure = deepcopy(g)                        # imported from copy module
    verts = list(closure.vertices())             # make indexable list
    n = len(verts)
    for k in range(n):
        for i in range(n):
            # verify that edge (i, k) exists in the partial closure
            if i != k and closure.get_edge(verts[i], verts[k]) is not None:
                for j in range(n):
                    # verify that edge (k, j) exists in the partial closure
                    if i != j != k and closure.get_edge(verts[k], verts[j]) is not None:
                        # if (i, j) not yet included, add it to the closure
                        if closure.get_edge(verts[i], verts[j]) is None:
                            closure.insert_edge(verts[i], verts[j])
    return closure

# The scheduling constraints impose restrictions on the order in which the tasks can be
# Topological Ordering
# 14.5.1 Topological Ordering
# Let G be a directed graph with n vertices.
# That is, a topological ordering is an ordering such that any directed path in G traverses 
# Technically, a Python dictionary provides O(1) expected time access
# Indeed, if the algorithm terminates without ordering all the vertices, 

def topological_sort(g):
    """Return a list of vertices of directed acyclic graph g in topological order.

    If graph g has a cycle, the result will be incomplete.
    """
    topo = []                                         # a list of vertices placed in topological order
    ready = []                                        # list of vertices that have no remaining constraints
    incount = {}
    for u in g.vertices():
        incount[u] = g.degree(u, False)               # parameter requests incoming degree
        if incount[u] == 0:                           # if u has no incoming edges
            ready.append(u)
    while len(ready) > 0:
        u = ready.pop()                               # u is free of constraints
        topo.append(u)                                # add u to the topological order