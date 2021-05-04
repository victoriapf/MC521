if __name__ == '__main__':
    n = int(input())
    s = input()
    rooms = [0] * 10
    for i in range(0, n):
        c = s[i]
        if(c == 'R'):
            last = len(rooms) - rooms[::-1].index(0) - 1
            rooms[last] = 1
        elif (c == 'L'):
            first = rooms.index(0)
            rooms[first] = 1
        else:
            rooms[int(c)] = 0
    print(*rooms, sep='')
