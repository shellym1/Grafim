INF = 99999


def FloydWarshall(matrix):
    newMat = [[0] * (len(matrix))] * (len(matrix))
    for i in range(len(newMat)):
        for j in range(len(newMat)):
            newMat[i][j] = matrix[i][j]
    print(newMat)

    for k in range(len(newMat)):
        for i in range(len(newMat)):
            for j in range(len(newMat)):
                if newMat[i][k] == INF or newMat[k][j]:
                    continue
                elif newMat[i][j] > newMat[i][k] + newMat[k][j]:
                    newMat[i][j] = newMat[i][k] + newMat[k][j]
    print(newMat)



    for i in range(1, len(newMat)):
        for j in range(len((newMat))):
            print(" the distance between" ,i, "to j", j, "is: ", newMat[i][j])






def main():

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
    #print(FloydWarshall(matrix2))

    graph1 = [[0, 1, 4, INF, INF, INF],
                   [INF, 0, 4, 2, 7, INF],
                   [INF, INF, 0, 3, 4, INF],
                   [INF, INF, INF, 0, INF, ],
                   [INF, INF, INF, 3, 0, INF],
                   [INF, INF, INF, INF, 5, 0]]


    mat = [[True, False, False, True, False, True, False],  #0
           [False, True, True, False, True, False, True],  #1
           [False, True, True, False, True, False, True],  #2
           [True, False, False, True, False, True, False], #3
           [False, True, True, False, True, False, True],  #4
           [True, False, False, True, False, True, False],  #5
           [False, True, True, False, True, False, True],  #6
           ]
    print(FloydWarshall(graph1))


if __name__ == '__main__':
    main()