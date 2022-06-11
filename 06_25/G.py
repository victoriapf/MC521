if __name__ == '__main__':
    for t in range(0, int(input())):
        n, x = map(int, input().split())
        a = sorted(list(map(int, input().split())))
        count = 0
        aws = 0
        for i in range(n-1, -1, -1):
            count += 1
            if a[i] * count >= x:
                aws += 1
                count = 0
        print(aws)
