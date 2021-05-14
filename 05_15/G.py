
def merge(odd, even):
    i = 0
    j = 0
    s = ''
    while i < len(even) and j < len(odd):
        if even[i] < odd[j]:
            s += str(even[i])
            i += 1
        elif even[i] > odd[j]:
            s += str(odd[j])
            j += 1
    if j == len(odd):
        s += (''.join(map(str, even[i:])))
    elif i == len(even):
        s += (''.join(map(str, odd[j:])))
    return s


if __name__ == '__main__':
    t = int(input())
    for i in range(0, t):
        s = input()
        odd = []
        even = []
        for j in range(len(s)):
            n = int(s[j])
            if n % 2:
                even.append(n)
            else:
                odd.append(n)
        print(merge(odd, even))
