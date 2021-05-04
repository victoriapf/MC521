def max_quasi_bin(n):
    quasi_bin = ''
    for i in range(len(n)):
        if(n[i] == '0'):
            quasi_bin += '0'
        else:
            quasi_bin += '1'
    return quasi_bin


if __name__ == '__main__':
    n = input()
    quasis = []
    while n != '0':
        quasi = max_quasi_bin(n)
        quasis.append(quasi)
        n = str(int(n) - int(quasi))
    print(len(quasis))
    print(*quasis)
