def toDollar(n, d):
    if n in d:  # ja calculei
        return d[n]
    else:
        d[n] = max(n, toDollar((n // 2), d) +
                   toDollar((n // 3), d) + toDollar((n // 4), d))
    return d[n]


if __name__ == '__main__':
    d = {}
    for i in range(12):
        d[i] = i
    for i in range(10):
        n = input()
        if(n == ''):
            break
        else:
            print(toDollar(int(n), d))
