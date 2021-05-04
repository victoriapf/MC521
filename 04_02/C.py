if __name__ == '__main__':
    n = int(input())
    enter = list(map(int, input().split()))
    out = list(map(int, input().split()))

    expected = [0] * n
    for i in range(0, n):
        expected[enter[i] - 1] = i

    fined = 0
    pos = expected[out[n - 1] - 1]
    for i in range(n - 2, -1, -1):
        car = out[i] - 1
        if int(expected[car]) < pos:
            pos = expected[car]
        else:
            fined += 1
    print(fined)
