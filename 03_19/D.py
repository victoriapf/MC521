if __name__ == '__main__':
    n = int(input())
    p = tuple(map(int, input().split()))
    sort = list(range(1, n+1))
    t = [0]*n
    for i in range(n):
        index = n - p[i]
        t[i] = sort[index]
    print(' '.join(map(str, t)))
