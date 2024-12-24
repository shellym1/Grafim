

#known roots
def isIsomorphic(T1, r1, T2, r2):
    if len(T1) != len(T2):
        return False
    generateCodes(T1, r1)
    generateCodes(T2, r2)
    if r1.code == r2.code:
        return True
    else:
        return False

def generateCodes(T, v):
    v.color = 'black'
    queue = []
    if v.degree == 1:
        v.code = '10'
    else:
        for u in T:
            if u.color == 'white':
                generateCodes(T, u)
                queue.append(u.code)
    sorted(queue)
    temp = []
    for i in queue:
        if len(queue) != 0:
            temp[i] = queue.pop(0)
    v.code = "1" + temp + "0"


#unknown root
def isIsomorphicWithoutRoot(T1, T2):
    roots1 = []
    roots2 = []
    roots1 = fire(T1)
    roots2 = fire(T2)


    if len(roots1) != len(roots2):
        return False
    r1 = roots1.pop(0)
    code1 = generateCodes(T1, r1)
    while len(roots2) != 0:
        r2 = roots2.pop(0)
        code2 = generateCodes(T2, r2)
        if code1 == code2:
            return True
    return False



def fire(T):
    radius = 0
    n = len(T)
    leaves = []
    diam = 0
    for i in range(n):
        if len(T(i)) == 1:
            leaves.append(i)
    while n > 2:
        radius += 1
        next_leaves = []
        for v in range(len(leaves)):
            u = T(v+1)
            if T(u) == 2:
                next_leaves.append(u)
            T.remove(v)
            n -=1
        leaves = next_leaves
    if n ==1:
        diam = 2*radius
    if n == 2:
        diam = 2*radius +1
    return T, radius, diam




def main():
    degree = [4, 3, 2, 1, 1, 1, 1, 1]




if __name__ == '__main__':
    main()