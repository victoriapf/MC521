import math

if __name__ == '__main__':
    n = int(input())
    control = 'f'
    for i in range(0, n):
        a = int(input())
        if(a % 2 == 0):
            print(int(a/2))
        else:
            if(control == 'f'):
                control = 'c'
                print(math.floor(a/2))
            elif(control == 'c'):
                control = 'f'
                print(math.ceil(a/2))
