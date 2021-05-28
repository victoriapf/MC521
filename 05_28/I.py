if __name__ == '__main__':
    n = int(input())
    for i in range(0, n):
        c, sum = map(int, input().split())
        if c >= sum:
            print(str(sum))
        else:
            k = int(sum/c)
            rest = sum % c
            cost = (rest * ((k+1)**2) + (c-rest)*(k**2))
            print(str(cost))
