import math
#בדיקת מספר רכיבי קשירות
INF = math.inf

def floydwarshal(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(len(matrix)):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
    return matrix

def connectComponentsOfGraphBoolean(matrix):
    arr = [0]*(len(matrix))
    counter = 0
    for i in range(len(matrix)):
        if arr[i] == 0:
            counter += 1
            arr[i] = counter
            for j in range(len(matrix)):
                if matrix[i][j] != INF:
                    arr[j] = counter
    return counter

def buildPathMatrix(matrix):
    n = len(matrix)
    floydwarshal(matrix)
    path = [0]*n
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != INF:
                path[i] = i,j
    return path







def main():
    INF = math.inf

    matrix2 = [
        [0, INF, 2, INF],
        [4, 0, 3, INF],
        [INF, INF, 0, 2],
        [INF, 1, INF, 0]
    ]

    print(floydwarshal(matrix2))
    print(connectComponentsOfGraphBoolean(floydwarshal(matrix2)))
    print(buildPathMatrix(matrix2))




if __name__ == '__main__':
    main()