if __name__ == '__main__':
    n = int(input())
    s = input()
    if(len(set(s.lower())) == 26):
        print('YES')
    else:
        print('NO')
