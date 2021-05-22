if __name__ == '__main__':
    s = ''
    r1, c1, r2, c2 = map(int, input().split())
    diff_row = (abs(r1-r2))
    diff_col = (abs(c1-c2))
    #### rook ####
    if(r1 == r2 or c1 == c2):
        s += '1 '
    else:
        s += '2 '
    #### bishop ####
    if(diff_row % 2 != diff_col % 2):
        s += '0 '
    elif(diff_row == diff_col):
        s += '1 '
    else:
        s += '2 '
    #### king ####
    s += str(max(diff_row, diff_col))
    print(s)
