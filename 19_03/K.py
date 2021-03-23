if __name__ == '__main__':
    r = int(input())
    i = 0
    while(i < r):
        n = int(input())
        p = list(map(int, input().split()))
        q = [0]*3
        found = False
        for j in range(1, n-1):
            if(p[j] > p[j-1] and p[j] > p[j+1]):
                q = [j, j+1, j+2]
                found = True
                break
        if(not(found)):
            print('NO')
        else:
            print('YES')
            print(' '.join(map(str, q)))
        i = i+1
