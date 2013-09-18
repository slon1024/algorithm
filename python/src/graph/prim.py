
nodes=list("ABCDEFGHI")
edges=[
    ('A', 'B', 4), ('B', 'C', 12), ('C', 'D', 7),
    ('D', 'E', 9), ('E', 'F', 10), ('F', 'G', 2),
    ('G', 'H', 1), ('H', 'A', 8), ('H', 'B', 11),
    ('H', 'I', 7), ('G', 'I', 6), ('I', 'C', 2),
    ('C', 'F', 4), ('D', 'F', 14)
]

class CustomFibonacciHeap():
    def __init__(self):
        self.__rows = []

    def insert(self, edge):
        """(CustomFibonacciHeap, tuple) -> void
        """
        self.__rows += [edge]

    def find_min(self):
        self.__rows.sort(key=lambda x: (x)[2])
        return (0, self.__rows[0])

    def find_min_and_delete(self):
        (key, data) = self.find_min()
        self.__rows.pop(key)
        return data



def prim(nodes, edges, node):
    """(list, list, str) -> list

    Prim's algorithm
    Find Minimum Spanning Tree
    >>>kruskal(list("ABC"), [('A', 'B', 4), ('B', 'C', 7), ('C', 'A', 5)], 'A')
    [('A', 'B', 4), ('C', 'A', 5)]
    """

    mst=[]
    visited=[node]
    heap = CustomFibonacciHeap()


    while len(visited) < len(nodes):
        for edge in edges:
            if ( (edge)[0] == node and (edge)[1] not in visited ) or  ( (edge)[1] == node and (edge)[0] not in visited ):
                heap.insert(edge)

        next_edge = heap.find_min_and_delete()
        next_node=(next_edge)[1] if (next_edge)[0] in visited else (next_edge)[0]
        if next_node in visited:
            continue

        visited += [next_node]
        mst     += [next_edge]
        node     = next_node

    return mst

print (prim(nodes, edges, 'G'))
