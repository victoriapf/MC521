if __name__ == '__main__':
    n, p = map(int, input().split())
    aws = 1
    while True:
        min_number = aws * ((2**0) + p)
        if min_number > n:
            aws = -1
            break
        elif min_number == n:
            break
        elif bin((n - aws * p)).count('1') <= aws:
            break
        aws += 1
    print(aws)
