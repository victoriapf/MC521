if __name__ == '__main__':
    n = int(input())
    slime = list(map(int, input().split()))
    dp = [0] * n
    print(sum(slime))
