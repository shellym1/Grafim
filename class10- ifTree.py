
def ifTree(degree):
    sum = 0
    v = len(degree)
    for i in range(len(degree)):
        sum += degree[i]

    if sum != 2*(v-1):
        return False

    tree = [0]* v
    j=0
    sorted(degree)
    for i in range(v):
        if degree[i] >1:
            j=i
    for i in range(v-2):
        tree[i] = j
        degree[j] -=1

        if degree[j] ==1:
            j+=1

    tree[v-1] = v
    return tree





def main():
    degree = [4, 3, 2, 1, 1, 1, 1, 1]
    print(ifTree(degree))


if __name__ == '__main__':
    main()
