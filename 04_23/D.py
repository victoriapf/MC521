if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    rest = 0
    last = 0
    for i in range(n):
        if a[i] == 0 or a[i] == last:
            last = 0
            rest += 1
        elif a[i] == 3:
            if(last != 0):
                last -= 3
            else:
                last = a[i]
    print(rest)
