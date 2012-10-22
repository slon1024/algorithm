class Forest():
    def __init__(self):
        """(Forest) -> void
        Initialize forest
        """
        self._sets={}

    def make(self, node):
        """(Forest, str) -> void

        Make new tree
        >>forest = Forest()
        >>forest.make('A')
        """
        self._sets[node] = node

    def find(self, node):
        """(Forest, str) -> str

        Returns a pointer to the tree containing node.

        >>>forest = Forest()
        >>>forest.make('A')
        >>forest.find('A')
        A
        """
        return self._sets[node]

    def union(self, node_a, node_b):
        """(Forest, str, str) -> void

        Unites the trees that contain node_a and node_b into a new tree that is union of these two trees.

        >>>forest = Forest()
        >>>forest.make('A')
        >>>forest.make('B')
        >>forest.union('A', 'B')
        >>forest.find('A') == forest.find('B')
        True
        """
        value_a = self._sets[node_a]
        value_b = self._sets[node_b]
        for key in self._sets.keys():
            if value_b == self._sets[key]:
                self._sets[key] = value_a

    
def kruskal(nodes, edges):
    """(list, list) -> list

    Find Minimum Spanning Tree
    >>>kruskal(list("ABC"), [('A', 'B', 4), ('B', 'C', 7), ('C', 'A', 5)])
    [('A', 'B', 4), ('C', 'A', 5)]
    """

    mst=[]
    forest=Forest()
    for node in nodes:
        forest.make(node) 
    sort_edges=sorted(edges, key=lambda x: (x)[2])
    
    for edge in sort_edges:
        if forest.find( (edge)[0] ) != forest.find( (edge)[1] ):
            mst += [edge] 
            forest.union((edge)[0], (edge)[1])

    return mst