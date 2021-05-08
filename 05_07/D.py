if __name__ == '__main__':
    n = int(input())
    days = [list(c for c in map(int,input().split())) for _ in range(n)]
    if(n == 1):
        print(max(days[0][0],days[0][1],days[0][2]))
    else:
        dp = [list(0 for _ in range(3)) for _ in range(n)]
        dp[0][0:n] = days[0][0:n]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][1],dp[i-1][2]) + days[i][0]
            dp[i][1] = max(dp[i-1][0],dp[i-1][2]) + days[i][1]
            dp[i][2] = max(dp[i-1][1],dp[i-1][0]) + days[i][2]
        print(max(dp[n-1][0],dp[n-1][1],dp[n-1][2]))



    
