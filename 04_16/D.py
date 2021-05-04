if __name__ == '__main__':
    n, t = map(int, input().split())
    q = (list(map(int, input().split())))
    time = 0
    start = 0
    books = 0
    for i in range(n):
        time += q[i]
        books += 1
        if time > t:
            time -= q[start]
            start += 1
            books -= 1
    print(books)
