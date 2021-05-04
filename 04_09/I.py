
if __name__ == '__main__':
    n = int(input())
    count = 0
    for a in range(1, n):
        for b in range(a, n):
            c = __import__('math').sqrt((a * a) + (b * b))
            if(int(c) == c and c <= n):
                count += 1
            elif(c > n):
                break
    print(count)
