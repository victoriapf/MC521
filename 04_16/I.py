if __name__ == '__main__':
    m = int(input())
    for i in range(m):
        s = input()
        out = ''
        for c in (''.join(set(s))):
            double = s.count(c + c)
            alone = s.count(c)
            if (alone - 2 * double) > 0:
                out += c
        print(''.join(sorted(out)))
