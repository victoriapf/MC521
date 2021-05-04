if __name__ == '__main__':
    q = int(input())
    for i in range(q):
        k, n, a, b = map(int, input().split())
        turns = k - n * b
        if (n * b >= k):
            turns = -1
        elif (n * a < k):
            turns = n
        else:
            turns = int(((k - n * b) - 1) / (a - b))
        print(turns)
