if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    sum = sum(a)
    if (sum % 3 != 0) or (n < 3):
        print(0)
    else:
        value = int(sum/3)
        third = aws = s = 0
        for i in range(n-1):
            s += a[i]
            if s == 2 * value:
                aws += third
            if s == value:
                third += 1

        print(aws)
