if __name__ == '__main__':
    n, k = map(int, input().split())
    option = list(map(int, input().split()))
    dp = [0] * k+1

    for i in range(k):
        for j in range(n):
            if i - op[j] >= 0:
                dp[i] += dp[i-op[j]]
        

    print(dp[lin - 1][col - 1])
