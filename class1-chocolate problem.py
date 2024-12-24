
def chocolateproblem(c):

    if c == 1:
        return 0
    elif c == 2:
        return 1
    else:
        clc = (c*(c-1)) / 2
        return clc




def main():
    c = 8
    print(chocolateproblem(c))


if __name__ == '__main__':
    main()