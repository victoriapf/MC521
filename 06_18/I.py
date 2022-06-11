if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    m = a[0]
    days = 1
    for i in range(1, n):
        m = max(a[i-1], m)
        if m == i:
            days += 1
    print(days)
