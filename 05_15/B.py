if __name__ == '__main__':
    n, x = map(int, input().split())
    where = 1
    watched = 0
    for i in range(0, n):
        r, l = map(int, input().split())
        time_left = (r-where) % x
        watched += (l - r) + 1 + time_left
        where = l + 1
    print(watched)