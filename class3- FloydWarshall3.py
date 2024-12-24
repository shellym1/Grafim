import math
INF = math.inf

def floydwarshal(matrix, values):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] ==0:
                matrix[i][j] = values[i]
            else:
                matrix[i][j] = values[i] + values[j]
    print(matrix )

    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i !=j:
                    matrix[i][j] = min(matrix[i][j], (matrix[i][k] + matrix[k][j]))
    print(matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i!=j:
                matrix[i][j] = (values[i] + matrix[i][j] + values[j]) / 2
    return matrix


'''
def buildPathMatrix(matrix, L):

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                matrix[i][j] = 0
            elif matrix[i][j] != INF :
                matrix[i][j] = L[i] + L[j]
    i=j=0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(len(matrix)):
                if matrix[i][j] != INF and matrix[i][k] + matrix[k][j] < matrix[i][j]:
                    matrix[i][k] = min(matrix[j][k], (matrix[k][j] + matrix[i][j]))
                #matrix[i][j] = min(matrix[i][j] , matrix[i][k] + matrix[k][j])
    i=j=0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j:
                matrix[i][j] = ( L[i] + matrix[i][j] + L[j] ) /2
    return matrix


def buildPathMatrix(matrix):
    for i in range(len(matrix)):  #+
        for j in range(len(matrix)):
            for k in range(len(matrix)):
                if matrix[i][k] != INF and matrix[k][j] != INF:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]

    for i in range(len(matrix)):  # min
        for j in range(len(matrix)):
            for k in range(len(matrix)):
                if matrix[i][k] != INF and matrix[k][j] != INF:
                    matrix[i][j] = min(matrix[i][k] , matrix[k][j])
                elif matrix[i][k] == INF:
                    matrix[i][j] = matrix[k][j]
                elif matrix[k][j] == INF:
                    matrix[i][j] = matrix[i][k]
                else:
                    matrix[i][j] = INF
    return matrix

'''







def main():
    INF = math.inf
    values = [1,7,10,5]
    matrix = [
        [0,1,INF,1],
        [1,0,1,INF],
        [INF,1,0,1],
        [1,INF,1,0]
    ]
    print(floydwarshal(matrix, values))


if __name__ == '__main__':
    main()