if __name__ == '__main__':
    n = int(input())
    s = sorted(list(map(int, input().split())))
    days = 0
    for i in range(0, n):
        minimal_set = s[i]
        if((days+1) <= minimal_set):
            days += 1
    print(days)
