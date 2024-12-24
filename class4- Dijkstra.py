

'''
class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def minDistance(self, dist):

        for v in range(self.V):
            for u in range(self.V):
                if self.graph[v][u] > 0:
                    if dist[v] > dist[u] + self.graph[v][u]:
                        dist[v] = dist[u] + self.graph[v][u]
    return
'''


def dijkstra(G, v, start):
    dist = [-1]* len(G) # Distance from start to others
    prev = [0] * len(G) # before last vertex in shortest path
    visit = ['false'] * len(G) #for every vertex we visited- we'll change the value to True
    minHeap = [0] * len(G)
    dist[start] = 0

    for i in range(len(G)):
        minHeap.insert(i, dist[i])

    while minHeap:
        for u in range(len(G)):
            if visit[u] == 'false' & dist[v] + G[v][u] < dist[u]:
                dist[u] = dist[v] + G[v][u]
                prev[u] = v
                minHeap.remove(u, dist[u])
            visit[v] == 'True'
    return dist

def main():
    G = [[0, 4, 1, -1],
		[-1, 0, -1, 1],
		[-1, -1, 0, 2],
		[-1, -1, -1, 0],
		]
    v = 4
    start = G[0][0]
    print(dijkstra(G, v,start ))


if __name__ == '__main__':
    main()