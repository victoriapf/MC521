if __name__ == '__main__':
    t = int(input())
    for i in range(0, t):
        n, x, a, b = map(int, input().split())
        max_dist = n - 1
        start_dist = abs(a-b)
        print(min(max_dist, start_dist+x))
