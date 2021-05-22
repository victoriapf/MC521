if __name__ == '__main__':
    t = int(input())
    for i in range(0, t):
        n = int(input())
        tel = input()
        first = tel.find('8')
        if((len(tel) < 11) or (first < 0)):
            print('NO')
        elif((n - first) < 11):
            print('NO')
        else:
            print('YES')
