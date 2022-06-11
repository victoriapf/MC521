if __name__ == '__main__':
    l, r, k = map(int, input().split())
    num = 1
    res = ''
    while (num < l):
        num *= k

    while (num <= r):
        res += str(num) + ' '
        num *= k
    if res == '':
        res = '-1'
    print(res)
