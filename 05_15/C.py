if __name__ == '__main__':
    n = int(input())
    a = sorted(list(map(int, input().split())))
    sum = 0
    for i in range(0, n):
        wanted = i + 1
        sum += abs(wanted - a[i])
    print(sum)
