if __name__ == '__main__':
    for i in range(0, int(input())):
        n, m, = map(int, input().split())
        if n == 1:
            if(m != 1):
                print('NO')
            else:
                print('YES')
        elif 1 < n <= 3:
            if(m > 3):
                print('NO')
            else:
                print('YES')
        else:
            print("YES")
