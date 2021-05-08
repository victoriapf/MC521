if __name__ == '__main__':
    n = int(input())
    cost = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = 0
    dp[1] = abs(cost[1] - cost[0])
    for i in range(2, n):
        dp[i] = min(abs(cost[i] - cost[i-1]) + dp[i-1],
                    abs(cost[i] - cost[i-2]) + dp[i-2])
    print(dp[n-1])
