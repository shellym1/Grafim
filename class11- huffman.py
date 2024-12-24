
def huffman(degree): #o(nlog(n))
    n = len(degree)
    tree = []
    for i in range(n):
        tree[i] = degree[i]
    first = 0
    while degree[first] > 1:
        first +=1
    vertex = 0
    numV = 1
    if n > 2:
        while (vertex < first):
            for j in range(len(degree[vertex])):
                tree[vertex].append(numV)
                tree[numV].append(vertex)
                numV +=1
            vertex +=1
            degree[vertex] -=1
    elif n==2:
        tree[0].add(1)
        tree[1].add(0)
    return tree


def huffman2(degree): #o(n)
    sorted(degree)
    n = len(degree)
    queue1 = []
    queue2 = []
    z=0
    z.right=0
    z.left = 0
    for i in range(n):
        queue1.append(degree(i))
    while queue1 + queue2 > 1:
        x = getmin(queue1, queue2)
        y = getmin(queue1, queue2)
        z.left = x
        z.right = y
        z = x + y
        queue2.append(z)
    if len(queue1) == 0:
        return queue2.pop(0)
    else:
        return queue1.pop(0)

def getmin(Q1, Q2):
    if len(Q1) == 0:
        return Q2.pop(0)
    elif len(Q2) ==0:
        return Q1.pop(0)
    elif Q1.index(0) < Q2.index(0):
        return Q1.pop(0)
    else:
        return Q2.pop(0)








def main():
    degree = [4, 3, 2, 1, 1, 1, 1, 1]
    print(huffman(degree))



if __name__ == '__main__':
    main()
