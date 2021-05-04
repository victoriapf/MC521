from itertools import permutations

if __name__ == '__main__':
    G = [list(map(int, input().split())) for _ in range(5)]
    aws = 0
    for a, b, c, d, e in permutations([0, 1, 2, 3, 4]):
        happy = G[a][b] + G[b][a] + G[c][d] + G[d][c]
        happy += G[b][c] + G[c][b] + G[d][e] + G[e][d]
        happy += G[c][d] + G[d][c]
        happy += G[d][e] + G[e][d]
        aws = max(aws, happy)
    print(aws)
