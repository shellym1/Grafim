
def BFS(G, source):
    INF = 9999
    n = len(G)
    dist = {}
    pred = {}
    color = {}


    for v in G:
        color[v] = 'white'
        dist[v] = -1
        pred[v] = None

    queue = []

    dist[source] = 0
    color[source] = 'grey'
    queue.append(source)

    while len(queue) >0:
        v = queue.pop(0)
        for u in G[v]:
            if color[u] == 'white':
                color[u] = 'grey'
                pred[u] = v
                dist[u] = dist[v] +1
                queue.append(u)
        color[v] = 'black'
    return (color,
            dist,
            pred)

'''
def checkConnectivity(color):
    for i in range(len(color)):
        if color[i] == 'white':
            return('true')
        else:
            return('false')
'''

def numberofConnections(G, color):
    connections = 1
    for i in range(len(color)):
        if color[i] == 'white':
            BFS(G, i)
            connections += 1
    return connections







def main():
    inf = 9999
    g = {"v1": ["v2", "v4"], "v2": ["v1", "v3"], "v3": ["v2"], "v4": ["v1", "v5", "v8"], "v5": ["v4", "v6", "v7", "v8"],
         "v6": ["v5", "v7"], "v7": ["v5", "v6", "v8"], "v8": ["v4", "v5", "v7"]}
    #print(BFS(g, 'v1'))

    #print(checkConnectivity(g, 'v1'))

    color,dist,pred = BFS(g, 'v1')
    print("color : ", color)
    #print("distance : ", dist)
    #print("pred : ", pred)
    #print(checkConnectivity(color))
    print(numberofConnections(g, color))


if __name__ == '__main__':
    main()
