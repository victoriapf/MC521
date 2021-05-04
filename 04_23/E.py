if __name__ == '__main__':
    n, m = map(int, input().split())
    d = [0] * m
    for i in range(n):
        c, x = map(str, input().split())
        d[int(c) - 1] = max(d[:int(c)]) + 1
    print(n - max(d))
