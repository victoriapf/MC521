if __name__ == '__main__':
    a = list(map(int, input().split()))
    aws = 0
    for c in input():
       aws += a[int(c)-1]
    print(aws) 
