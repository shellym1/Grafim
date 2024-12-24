
def bipartite(G, source):
    v= len(G)
    color = [-1] * v
    color[source] = 1
    queue = []
    queue.append(source)
    while len(queue) !=0:
        u = queue.pop(0)
        if G[u][u] == 1:
            return False
        for i in range(v):
            if G[u][i] and color[i] == -1 and len(queue) !=0 :
                color[i] = 1 - color[u]
                queue.pop(i)
            elif  G[u][i] and color[i] == color[u]:
                return False
    return True





def main():
    G = [[0,1,0,1],
         [1,0,1,0],
         [0,1,0,1],
         [1,0,1,0]]
    s = 0
    print(bipartite(G, s))



if __name__ == '__main__':
    main()




