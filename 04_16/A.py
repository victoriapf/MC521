if __name__ == '__main__':
    n, k = map(int, input().split())
    q = sorted(map(int, input().split()))[int(n / 2):n]
    median = q[0]
    op = 1
    for i in range(1, len(q)):
        if((q[i] - median) * op <= k):
            k -= (q[i] - median) * op
            median = q[i]
        else:
            break
        op += 1
    print(median + int(k / op))
