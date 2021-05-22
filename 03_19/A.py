if __name__ == '__main__':
    s = input()
    s = s.split()

    bag_1 = int(s[0])
    bag_2 = int(s[1])
    bag_3 = int(s[2])
    bag_4 = int(s[3])
    total_candies = (bag_1+bag_2+bag_3+bag_4)

    if(total_candies % 2 != 0):
        print('NO')
    elif((bag_1) == (bag_2+bag_3+bag_4)):
        print('YES')
    elif((bag_2) == (bag_1+bag_3+bag_4)):
        print('YES')
    elif((bag_3) == (bag_1+bag_2+bag_4)):
        print('YES')
    elif((bag_4) == (bag_1+bag_2+bag_3)):
        print('YES')
    elif((bag_1+bag_2) == (bag_3+bag_4)):
        print('YES')
    elif((bag_1+bag_3) == (bag_2+bag_4)):
        print('YES')
    elif((bag_1+bag_4) == (bag_2+bag_3)):
        print('YES')
    else:
        print('NO')
