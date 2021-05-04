if __name__ == '__main__':
    n, m = map(int, input().split())
    j = 0
    for i in range(n):
        if(i % 2 == 0):
            print('#'*m)
        elif(j % 2 == 0):
            print('.'*(m-1)+'#')
            j += 1
        else:
            print('#' + '.'*(m-1))
            j += 1
