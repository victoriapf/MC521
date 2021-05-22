

def win(query):
    if (query.count(2048) > 0):
        return True
    return False


def lost(query):
    if (query.count(1) > 1):
        return False
    elif (query.count(2) > 1):
        return False
    elif (query.count(4) > 1):
        return False
    elif (query.count(8) > 1):
        return False
    elif (query.count(16) > 1):
        return False
    elif (query.count(32) > 1):
        return False
    elif (query.count(64) > 1):
        return False
    elif (query.count(128) > 1):
        return False
    elif (query.count(256) > 1):
        return False
    elif (query.count(512) > 1):
        return False
    elif (query.count(1024) > 1):
        return False
    else:
        return True


if __name__ == '__main__':
    r = int(input())
    j = 0
    while(j < r):
        n = int(input())
        q = (list(map(int, input().split())))
        q.sort()
        if(win(q)):
            print('YES')
        else:
            last_join = 0
            while(not(lost(q))):
                for i in range(n-1, 0, -1):
                    if(q[i] == q[i-1]):
                        new_q = [0]*(n-1)
                        new_q[i-1] = 2*q[i]
                        if(i > 0):
                            new_q[0:i-1] = q[0:i-1]
                        if(i < n):
                            new_q[i:n-1] = q[i+1:n]
                        q = new_q
                        n = n-1
                        last_join = new_q[i-1]
                        break
                if(last_join == 2048):
                    break
            if(last_join == 2048):
                print('YES')
            else:
                print('NO')
        j = j+1
