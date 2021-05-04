if __name__ == '__main__':
    n, k = (map(int, input().split()))
    s = input()
    if k == 0:
        print(s)
    elif n == 1 and k > 0:
        print(0)
    else:
        number = ''
        changed = 0
        for i in range(0, n):
            if(changed == k):
                number = number + s[i]
            elif i == 0:
                number = '1'
                if s[0] != '1':
                    changed = changed+1
            elif s[i] != '0':
                number = number + '0'
                changed = changed+1
            else:
                number = number + s[i]
        print(number)
