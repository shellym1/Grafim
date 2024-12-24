from heapq import heappop, heappush
'''
def singlesource(graph, source):
    INF = 9999
    dist = {k: INF for k in graph}
    dist[0] = 0
    parent = {k: None for k in graph}

    for v in range(len(graph)):
        for u in range(len(graph)):
            if dist[v] > dist[u] + graph(u, v):
                dist[v] = dist[u] + graph(u, v)
                parent[v] = u
'''


def dijkstra(graph,source):
    INF = 9999
    dist = [INF] * len(graph)
    parent = [None] * len(graph)
    dist[source] = 0

    queue = [(0, source)]
    '''
    for i in range(len(graph)):
        queue.append(graph(i,i))
    dist[source] = 0
'''
    while queue:
        u_dist, u = heappop(queue)
        if u_dist > dist[u]:
            continue
        for v in range(len(graph)):
            if graph[u][v] != INF:
                new_dist = dist[u] + graph[u][v]
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    parent[v] = u
                    heappush(queue, (new_dist, v))
        return dist, parent
        '''
        queue.remove(u)
        for v in queue:
            if dist[v] > dist[u] + graph(u, v):
                dist[v] = dist[u] + graph(u, v)
                parent[v] = u
    return dist, parent
'''







def main():
    INF = 9999

    matrix2 = [
        [0, INF, -2, INF],
        [4, 0, 3, INF],
        [INF, INF, 0, 2],
        [INF, -1, INF, 0]
        ]

    graph = [[0, 5, INF, 10],
            [INF, 0, 3, INF],
            [INF, INF, 0, 1],
            [INF, INF, INF, 0]
            ]

    INF = 9999  # Represents no connection

    graph2 = [
        # 0     1     2     3
        [0, 5, INF, 10],  # Node 0 connections
        [INF, 0, 3, INF],  # Node 1 connections
        [INF, INF, 0, 1],  # Node 2 connections
        [INF, INF, INF, 0]  # Node 3 connections
    ]

    dist, parent = dijkstra(graph2, 0)
    print("Distances from source:", dist)
    print("Parents:", parent)

if __name__ == '__main__':
    main()