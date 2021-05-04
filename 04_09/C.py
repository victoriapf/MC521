if __name__ == '__main__':
    t = int(input())
    for i in range(0, t):
        n = int(input())
        rooms = input()
        left = rooms.find('1')
        rigth = rooms.rfind('1')
        if((left > -1) or (rigth > -1)):
            qtd = 2 * (max((n - left), (rigth + 1)))
        else:
            qtd = n
        print(qtd)
