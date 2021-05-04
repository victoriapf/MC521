if __name__ == '__main__':

    while (s=input()):
        if s == '':
            break
        else:
            n = int(s)
            m = (list(map(int, input().split())))
            color = [[0] * 100 for _ in range(100)]
            smoke = [[0] * 100 for _ in range(100)]
            for i in range(n):
                color[i][i] = m[i]
            for i in range(2, n):
                for j in range(0, n - i + 1):
                    for k in range(j, j + i - 1):
                        sm = smoke[j][k] + smoke[k + 1][j + i - 1] + color[j][k] * color[k + 1][j + i - 1]
                        cl = (color[j][k] + color[k + 1][j + i - 1]) % 100
                        if(sm < smoke[j][j + i - 1]):
                            smoke[j][j + i - 1] = sm
                            color[j][j + i - 1] = cl

            print(smoke[0][n - 1])
