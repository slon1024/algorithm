
def floyd_warshall(graph):
    loop=range(len(graph))
    for i in loop:
        for j in loop:
            for k in loop:
                graph[j][k] = min( graph[j][k], graph[j][i] + graph[i][k])

    return graph



count=7
infinity=9999999

graph=[ [infinity for i in range(count)] for x in range(count)]
graph[0][3]=30;
graph[1][2]=15;
graph[2][3]=5;
graph[4][5]=20;
graph[5][6]=5;
graph[6][3]=25;
graph[0][1]=10;
graph[1][4]=40;
graph[2][4]=20;
graph[4][6]=10;


graph=floyd_warshall( graph )
for i in range(len(graph)):
    for j in range(len(graph)):
        if graph[i][j] == infinity:
            print i, "-->", j, " ucnreable!"
        elif i != j:
            print i, "-->", j, "=", graph[i][j]

