if __name__ == '__main__':
    r = int(input())
    j = 0
    while(j < r):
        n = int(input())
        a, b, c = map(int, input().split())
        q = input()
        s = ['X'] * n
        wins = 0
        for i in range(0, len(q)):
            char = q[i]
            if (char == 'R' and b > 0):
                b = b-1
                s[i] = 'P'
                wins = wins+1
            elif(char == 'P' and c > 0):
                c = c-1
                s[i] = 'S'
                wins = wins+1
            elif(char == 'S' and a > 0):
                a = a-1
                s[i] = 'R'
                wins = wins+1
        subs = 0
        count = s.count('X')
        while(count > 0):
            subs = s.index('X', subs, len(s))
            if(a > 0):
                a = a-1
                s[subs] = 'R'
            elif(b > 0):
                b = b-1
                s[subs] = 'P'
            elif(c > 0):
                c = c-1
                s[subs] = 'S'
            count = count - 1
        if(wins >= n/2):
            print('YES')
            print(''.join(map(str, s)))
        else:
            print('NO')
        j = j+1
