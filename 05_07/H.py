
def knapsack(W, wt, val, n):

    t = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(W + 1):
            # nao existe como incluir mais coisa
            if i == 0 or W == 0:
                t[i][j] = 0
            # retorna caso maximo entre (item incluido e nao incluido)
            elif wt[i - 1] <= j:
                t[i][j] = max(val[i - 1] + t[i - 1][j - wt[i - 1]],
                              t[i - 1][j])
            # nao cabe mais, nao inclui o item
            else:
                t[i][j] = t[i - 1][j]

    return t[n][W]


if __name__ == '__main__':
    N, S = map(int, input().split())
    val = (N) * [0]
    w = (N) * [0]
    for i in range(0, N):
        w[i], val[i] = map(int, input().split())
    if(N == 1):
        if(S >= w[0]):
            print(val[0])
        else:
            print(0)
    else:
        w, val = (list(t) for t in zip(*sorted(zip(w, val))))
        print(knapsack(S, w, val, N))
