
'''
def fire(tree):
    n = len(tree)
    nVert = n

    queueLeaves = []
    degree = [0]*n
    level = [0]*n
    radius = 0
    diam = 0
    centers = []

    for i in range(n):
        degree[i] = tree[i]
        if degree[i] == 1:
            queueLeaves.append(i)

    while nVert > 2:
        for i in range(len(queueLeaves)):
            leaf = queueLeaves.pop(0)
            degree[leaf] = 0
            nVert -= 1
            for j in range(len(leaf)):
                v = tree[leaf]
                degree -=1
                tree.remove(leaf)
                if degree[v] ==1:
                    queueLeaves.append(v)
    radius +=1
    if len(queueLeaves) ==2:
        centers.append(queueLeaves.pop(0))
        centers.append(queueLeaves.pop(0))
        radius +=1
        diam = 2 * radius - 1
    else:
        centers.append(queueLeaves.pop(0))
        radius += 1
        diam = 2 * radius

    print(centers, radius, diam)
'''

def fire(T):
    radius = 0
    n = len(T)
    leaves = []
    diam = 0
    for i in range(n):
        if len(T(i)) == 1:
            leaves.append(i)
    while n > 2:
        radius += 1
        next_leaves = []
        for v in range(len(leaves)):
            u = T(v+1)
            if T(u) == 2:
                next_leaves.append(u)
            T.remove(v)
            n -=1
        leaves = next_leaves
    if n ==1:
        diam = 2*radius
    if n == 2:
        diam = 2*radius +1
    return T, radius, diam






def main():
    inf = 999
    '''
    *(0) - --(1) - --(2) - --(3) - --(4)
    * |
    *(6) - --(5) - --(7)
    '''
    T = {(1,6), (0,2), (1,3), (2,4),(3), (6,7), (0,5), (5)}
    matrix = [[inf, 1, inf, inf, inf, inf, inf, inf],
        [0, inf, 2, inf, inf, inf, inf, inf],
        [inf, 1, inf, 3, inf, 5, inf, inf],
        [inf, inf, 2, inf, 4, inf, inf, inf],
        [inf, inf, inf, 3, inf, inf, inf, inf],
        [inf, inf, 2, inf, inf, inf, 6, 7],
        [inf, inf, inf, inf, inf, 5, inf, inf],
        [inf, inf, inf, inf, inf, 5, inf, inf]]

    print(fire(T))



if __name__ == '__main__':
    main()
