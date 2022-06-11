if __name__ == '__main__':
    x = 0
    for i in range(0, int(input())):
        s = input()
        if(s.count('+') > 0):
            x += 1
        else:
            x -= 1
    print(x)
