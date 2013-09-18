
nodes=list("ABCDEFGHI")
edges=[
 ('A', 'B', 4), ('B', 'C', 8), ('C', 'D', 7),
 ('D', 'E', 9), ('E', 'F', 10), ('F', 'G', 2),
 ('G', 'H', 1), ('H', 'A', 8), ('H', 'B', 11),
 ('H', 'I', 7), ('G', 'I', 6), ('I', 'C', 2),
 ('C', 'F', 4), ('D', 'F', 14)
 
]

def prim(nodes, edges):
    """
    Prim's algorithm
    """
    mst=[]
    visited_nodes=[]
    live_edges=[]
    node=nodes[0]
    live_edges = loop(node, edges, visited_nodes, live_edges)

    for i in range(len(nodes) - 1):
        live_edges = loop(node, edges, visited_nodes, live_edges)

        nodelive_edges[0]



    return mst
    

def find_neighbors(node, edges, visited):
    result=[]
    for edge in edges:
        if ( (edge)[0] == node and (edge)[1] not in visited ) or  ( (edge)[1] == node and (edge)[0] not in visited ):
            result += [edge]
    return result



def loop(node, edges, visited_nodes, live_edges):
    neighbors = find_neighbors(node, edges, visited_nodes)
    for neighbor in neighbors:
        if neighbor not in live_edges:
            live_edges += [neighbor]



    live_edges.sort(key=lambda x: (x)[2] )

    return live_edges


prim(nodes, edges)
  
#print find_neighbors('A', edges, [])
#print find_neighbors('C', edges, ['I','F'])
#print find_neighbors('B', edges, visited)




