if __name__ == '__main__':
    t = int(input())
    for i in range(0, t):
        string = input()
        R, P, S = string.count("R"), string.count("P"), string.count("S")
        if(max(R, S, P) == R):
            print('P'*len(string))
        elif(max(R, S, P) == P):
            print('S'*len(string))
        else:
            print('R'*len(string))
