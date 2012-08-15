
def roy_warshall(graph):
    length=len(graph)
    for i in range(length):
        for j in range(length):
            for k in range(length):
                if(graph[j][k] == 0):
                    graph[j][k] = graph[j][i]*graph[i][k]
           
    return graph

