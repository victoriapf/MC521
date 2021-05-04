if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        C = list(map(int, input().split()))
        dp = [0] * N
        if (N == 0):
            print("Case " + (str(i + 1)) + ": 0")
            continue
        else:
            dp[0] = C[0]
            if (N >= 2):
                dp[1] = max(C[0], C[1])
            if (N >= 3):
                for j in range(2, N):
                    dp[j] = max(dp[j - 1], dp[j - 2] + C[j])
        print("Case " + (str(i + 1)) + ": " + str(dp[N - 1]))
