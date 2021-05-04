if __name__ == '__main__':
    n, m = map(int, input().split())
    ones = input().count('-1')
    x = min(n - ones, ones) * 2
    for i in range(m):
        l, r = map(int, input().split())
        c = int(((r - l) % 2) and ((r - l) < x))
        print(c)
