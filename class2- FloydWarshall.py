
#רכיב קשירות 1
INF = 99999
def FloydWarshall(matrix):
    newMat = [[0] * (len(matrix))] * (len(matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            newMat[i][j] = matrix[i][j]

    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if newMat[i][k] == INF or newMat[k][j]:
                    continue
                elif matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
    return matrix



def numberofConnections(matrix):
    C = [0]* len(matrix)
    '''
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == True:
                C[i] += 1
       '''
    counter =0
    for i in range(len(matrix)):
        if C[i] == 0:
            counter +=1
            C[i] = counter
        for j in range(i+1, len(matrix)):
            if C[j] == 0 and matrix[i][j]:
                C[j] = counter
    return C




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
    print(FloydWarshall(matrix2))


    mat = [[True, False, False, True, False, True, False],  #0
           [False, True, True, False, True, False, True],  #1
           [False, True, True, False, True, False, True],  #2
           [True, False, False, True, False, True, False], #3
           [False, True, True, False, True, False, True],  #4
           [True, False, False, True, False, True, False],  #5
           [False, True, True, False, True, False, True],  #6
           ]
    #print(numberofConnections(mat))


if __name__ == '__main__':
    main()