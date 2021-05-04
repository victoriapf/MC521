
if __name__ == '__main__':
    t = int(input())
    for i in range(0, t):
        a, b, c = map(int, input().split())
        first_take = min(b, int(c / 2))
        second_take = min(int((b - first_take) / 2), a)
        print(3 * (first_take + second_take))
