from itertools import chain

if __name__ == '__main__':
    n = int(input())
    tab = [list(c == '#'for c in input()) for _ in range(n)]
    flag = {True}.issubset(chain.from_iterable(tab))
    if(flag):
        for i in range(1, n-1):
            for j in range(1, n-1):
                if tab[i-1][j] and tab[i][j-1] and tab[i][j] and tab[i][j+1] and tab[i+1][j]:
                    tab[i-1][j] = False
                    tab[i][j-1] = False
                    tab[i][j] = False
                    tab[i][j+1] = False
                    tab[i+1][j] = False
        flag = {True}.issubset(chain.from_iterable(tab))
    if(flag):
        print('NO')
    else:
        print('YES')
