
def MaxSub(mat):
    n = len(mat) #שורה
    m = len(mat[0]) #עמודה
    maxsum = 0
    ii = 0
    jj = 0
    kk=0
    ll=0
    for i in range(n):
        for j in range(m):
            k=i
            for k in range(n):
                l=j
                for l in range(m):
                    sum =0
                    x=i
                    for x in range(k):
                        y=j
                        for y in range(l):
                            sum += mat[x][y]
                        if (sum > maxsum):
                            maxsum = sum
                            ii = i
                            jj = j
                            kk = k
                            ll = l
    return maxsum, ii, jj, kk, ll







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


'''
def MaxSubMatrix(mat):
    n = len(mat) #שורה
    m = len(mat[0]) #עמודה
    maxsum =0

    for i in range(n):
        j=i
        for j in range(n):
            arr = m
            k=i
            for k in range(j):
                for l in range(m):
                    best = findMaxSum(mat)
        if best[0] > maxsum:
            maxsum = best[0]
            ii = i
            jj = best[1]
            kk = j
            ll = best[2]
    return maxsum, ii, jj, kk, ll
'''

'''
def MaxSubMatrix(mat):
    n = len(mat) #שורה
    m = len(mat[0]) #עמודה
    subsum=[0] * n
    maxsum =0

    for i in range(n):
        for j in range(m):
            subsum = mat[i][0] + mat[i][j]
            if maxsum < subsum:
                maxsum = subsum
    return maxsum, i, j
'''


def kadane(arr, start, finish, n):
    # initialize sum, maxSum and
    Sum = 0
    maxSum = -999999999999
    i = None

    # Just some initial value to check
    # for all negative values case
    finish[0] = -1

    # local variable
    local_start = 0

    for i in range(n):
        Sum += arr[i]
        if Sum < 0:
            Sum = 0
            local_start = i + 1
        elif Sum > maxSum:
            maxSum = Sum
            start[0] = local_start
            finish[0] = i

    # There is at-least one
    # non-negative number
    if finish[0] != -1:
        return maxSum

    # Special Case: When all numbers
    # in arr[] are negative
    maxSum = arr[0]
    start[0] = finish[0] = 0

    # Find the maximum element in array
    for i in range(1, n):
        if arr[i] > maxSum:
            maxSum = arr[i]
            start[0] = finish[0] = i
    return maxSum


# The main function that finds maximum
# sum rectangle in M[][]


def findMaxSum(M):
    global ROW, COL
    ROW = 4
    COL = 5

    # Variables to store the final output
    maxSum, finalLeft = -999999999999, None
    finalRight, finalTop, finalBottom = None, None, None
    left, right, i = None, None, None

    temp = [None] * ROW
    Sum = 0
    start = [0]
    finish = [0]

    # Set the left column
    for left in range(COL):

        # Initialize all elements of temp as 0
        temp = [0] * ROW

        # Set the right column for the left
        # column set by outer loop
        for right in range(left, COL):

            # Calculate sum between current left
            # and right for every row 'i'
            for i in range(ROW):
                temp[i] += M[i][right]

            # Find the maximum sum subarray in
            # temp[]. The kadane() function also
            # sets values of start and finish.
            # So 'sum' is sum of rectangle between
            # (start, left) and (finish, right) which
            # is the maximum sum with boundary columns
            # strictly as left and right.
            Sum = kadane(temp, start, finish, ROW)

            # Compare sum with maximum sum so far.
            # If sum is more, then update maxSum
            # and other output values
            if Sum > maxSum:
                maxSum = Sum
                finalLeft = left
                finalRight = right
                finalTop = start[0]
                finalBottom = finish[0]

    # Prfinal values
    print("(Top, Left)", "(", finalTop,
          finalLeft, ")")
    print("(Bottom, Right)", "(", finalBottom,
          finalRight, ")")
    print("Max sum is:", maxSum)





def main():
    '''
    mat = [[2, 1, -3, -4, 5],
         [0, 6, 3, 4, 1],
         [2, -2 -1, 4, -5],
         [-3, 3, 1, 0, 3],
         ]
    return(MaxSubMatrix(mat))
    #return(MaxSub(mat))
    '''

    # Driver Code

    M = [[1, 2, -1, -4, -20],
         [-8, -3, 4, 2, 1],
         [3, 8, 10, 1, 3],
         [-4, -1, 1, 7, -6]]

    # Function call
    findMaxSum(mat)

if __name__ == '__main__':
    main()