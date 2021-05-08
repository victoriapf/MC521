if __name__ == '__main__':
    lin, col = map(int, input().split())
    tab = [list(c for c in input()) for _ in range(lin)]
    dp = [list(0 for _ in range(col)) for _ in range(lin)]

    dp[0][0] = 1

    for i in range(0, lin):
        for j in range(0, col):
            if tab[i][j] == ".":
                dp[i][j] += (dp[i-1][j] + dp[i][j-1])
                dp[i][j] %= 10 ** 9 + 7

    print(dp[lin - 1][col - 1])
