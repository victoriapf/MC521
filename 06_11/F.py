import math

if __name__ == '__main__':
    t = int(input())
    for i in range(0, t):
        a, b, c, d, k = map(int, input().split())
        x = math.ceil(a/c)
        y = math.ceil(b/d)
        if (x+y) > k:
            print(-1)
        else:
            print(x, y)
