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





def main():
    '''
    A = [1,2,-5]
    print(findMaxSum(A))

    A = [-6,3,-10,100,-18,20,-2]
    print(findMaxSum(A))
    '''
    B = [10,2,-5,8,-100,350,-80,1,2,3]
    print(findMaxSum(B))


if __name__ == '__main__':
        main()