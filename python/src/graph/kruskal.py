class Forest():
    def __init__(self):
        self._sets={}

    @property
    def keys(self):
        return self._sets.keys()

    def make(self, node):
        self._sets[node] = node
       

    def find(self, node):
        return self._sets[node]

    def union(self, node_a, node_b):
        value_a = self._sets[node_a]
        value_b = self._sets[node_b]
        for key in self.keys:
            if value_b == self._sets[key]:
                self._sets[key] = value_a
    
def kruskal(nodes, edges):
    """
    (list, list) -> list

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
