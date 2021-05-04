if __name__ == '__main__':
    n = int(input())
    q = (list(map(int, input().split())))
    index = 0
    for i in range(n-1, 0, -1):
        if(q[i-1] > q[i]):
            index = i
            break
    print(index)
