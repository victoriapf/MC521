if __name__ == '__main__':
    n, m = map(int, input().split())
    sweets = sorted(list(map(int, input().split())))
    add = sweets[0]
    print(sweets[0], end=' ')
    for i in range(1, n):
        add += sweets[i]
        sweets[i] = add
        if(i >= m):
            sweets[i] += sweets[i-m]
        print(sweets[i], end=' ')
