if __name__ == '__main__':
    n = int(input())
    changes = {}
    for i in range(0, n):
        old, new = input().split()
        first = changes.get(old)
        if first:
            changes.pop(old)
            changes[new] = first
        else:
            changes[new] = old
    print(len(changes))
    for new, old in changes.items():
        print(old, new)
