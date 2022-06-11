if __name__ == '__main__':
    likeability = list(map(int, input().split()))
    s = input().lower()
    add = [0] * len(s)
    add[0] = likeability[ord(s[0])-97]
    for i in range(1, len(s)):
        add[i] = add[i-1] + likeability[ord(s[i])-97]

    mat = {}
    for i in range(26):
        mat[i] = {}
    mat[ord(s[0])-97][add[0]] = 1
    res = 0

    for i in range(1, len(s)):
        chr = ord(s[i])-97
        if add[i-1] in mat[chr]:  # nao precisa somar o char atual
            res += mat[chr][add[i-1]]
        if add[i] in mat[chr]:
            mat[chr][add[i]] = mat[chr][add[i]]+1
        else:
            mat[chr][add[i]] = 1

print(res)
