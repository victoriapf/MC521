if __name__ == '__main__':
    likes = list(map(int, input().split()))
    s = input()
    r = [{} for i in range(26)]
    j = 1
    res = 0
    sum = [0] * (10 ** 5 + 1)
    for i in s:
        i = ord(i) - ord('a')
        sum[j] = sum[j - 1] + likes[i]
        if sum[j - 1] in r[i]:
            res += r[i][sum[j - 1]]
        if sum[j] in r[i]:
            r[i][sum[j]] += 1
        else:
            r[i][sum[j]] = 1
        j += 1
    print(res)