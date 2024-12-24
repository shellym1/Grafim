#חישוב סכום משקלים על הקודקודים והצלעות


INF = 99999


def LastFloydWarshall(matrix, values):

    print("GIVEN ORIGINAL MATRIX: ")
    print((matrix))
    temp = [[0] * (len(matrix))] * (len(matrix))

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                temp[i][j] = values[i]
            elif matrix[i][j] > 0 & matrix[i][j] != INF:
                temp[i][j] = 2 * matrix[i][j] + values[i] + values[j]
            if matrix[i][j] == INF:
                temp[i][j] = INF

    print(temp)

    print("FOLLOWING FLOYD WARSHALL ALGO (WITH WRONG WEIGHTS): ")
    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i !=j:
                    temp[i][j] = min(temp[i][j], temp[i][k] + temp[k][j])
    print(temp)

    print("FIXING WRONG WEIGHTS BY (V[SRC] + TEMP[SRC][DST] + V[DST])/2 "

          )

    solution = [[0] * (len(matrix))] * (len(matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j:
                solution[i][j] = (values[i] + temp[i][j] + values[j]) / 2
            else:
                solution[i][j] = values[i]
    return solution





def main():
    values = [1, 7, 10, 5]
    matrix = [[0, 5, INF, 20],
        [5, 0, 10, INF],
        [INF, 10, 0, 15],
        [20, INF, 15, 0]]

    print(LastFloydWarshall(matrix, values))



if __name__ == '__main__':
    main()