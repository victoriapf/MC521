if __name__ == '__main__':
    n, m, = map(int, input().split())
    x = 2 * n
    y = 3 * m
    i = 0

    while (i < max(n, m)):
        if (i % 6 == 0):
            if(i < n) and ((x+2) <= (y+3)):
                x += 2
            elif(i < m) and ((y+3) < (x+2)):
                y += 3
        i += 6
    print(max(x, y))
