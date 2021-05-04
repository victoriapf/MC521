if __name__ == '__main__':
    n, m = map(int, input().split())

    time = [0]*n
    for i in range(n):
        c, t = map(int, input().split())
        if(i > 0):
            time[i] = time[i-1] + c*t
        else:
            time[i] = c*t

    q = list(map(int, input().split()))
    i = 0
    for t in q:
        if(t <= time[i]):
            print(i+1)
        else:
            while((t > time[i]) and (i < n)):
                i += 1
            print(i+1)
