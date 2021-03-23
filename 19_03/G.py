if __name__ == '__main__':
    r = int(input())
    j = 0
    while(j < r):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        c = list(map(lambda i, j: (i - j), b, a))
        stop = False
        last_dif = 0
        continuity = True
        for i in range(0, len(c)):
            if(c[i] == 0 and last_dif != 0):
                continuity = False
            if(c[i] < 0):
                stop = True
                break
            if(c[i] != 0 and last_dif == 0):
                last_dif = c[i]
            elif(c[i] != 0 and last_dif != c[i]):
                stop = True
                break
            elif(c[i] != 0 and last_dif == c[i] and not(continuity)):
                stop = True
                break
        if(stop):
            print('NO')
        else:
            print('YES')
        j = j+1
