
#class5-import
def findMaxSum(A):
    max = A[0]
    temp_max = A[0]
    i=0
    while A[i] < 0:
        max = A[i+1]
        temp_max = A[i+1]
        i+=1

    for j in range(i, len(A)):
        if j+1 != len(A):
            temp_max += A[j+1]

            if max < temp_max:
                max = temp_max
        if temp_max < 0:
            temp_max = 0

    return max



def FuelStationProblem(a,b):
    c = [0] * len(a)
    sumC = 0
    minusC = [0] * len(c)
    for i in range(len(a)):
        c[i] = a[i] - b[i]
    bestC = findMaxSum(c)
    for i in range(len(c)):
        sumC = sumC + c[i]
    for i in range(len(c)):
        minusC[i] = -c[i]
    bestMinusSumC = findMaxSum(minusC)
    maxSum = max(bestC, sumC + bestMinusSumC)
    return maxSum






def main():
    a = [3,6,2,8]
    b=[5,4,3,4]
    print(FuelStationProblem(a,b))

if __name__ == '__main__':
    main()