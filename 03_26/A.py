from itertools import combinations_with_replacement

if __name__ == '__main__':
    n, x = (map(int, input().split()))
    q = (list(map(int, input().split())))
    possibilities = 0
    tam = n
    for a in range(1, x+1):
        l = [0]*(n)
        newQ = q
        tam = n
        for b in range(a, x+1):
            j = 0
            error = False
            for i in range(0, tam):
                if(newQ[i] < a or newQ[i] > b):
                    if((j > 0) and (l[j-1] > newQ[i])):
                        error = True
                        break
                    else:
                        l[j] = newQ[i]
                        j += 1
            if(not error):
                possibilities += 1
                newQ = l[0:j]
                tam = j
    print(possibilities)
