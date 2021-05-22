if __name__ == '__main__':
    t = int(input())
    for i in range(0, t):
        n = int(input())
        odd_outer_change = 0
        even_outer_change = 0
        for _ in range(n):
            s = input()
            n_1 = s.count('1')
            n_0 = len(s) - n_1
            if (len(s) % 2 != 0):
                odd_outer_change += 1
            elif not((n_1 % 2 == 0) and (n_0 % 2 == 0)):
                even_outer_change += 1

        if((even_outer_change % 2 != 0) and (odd_outer_change == 0)):
            print(n-1)
        else:
            print(n)
