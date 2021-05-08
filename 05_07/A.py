if __name__ == '__main__':
    n, m=map(int,input().split())
    s=[input()for _ in range(n)]
    faces = 0
    face_set = {'f','a','c','e'}
    for i in range(n-1):
        for j in range(m-1):
            if {s[i][j],s[i+1][j],s[i][j+1],s[i+1][j+1]} == face_set:
                faces += 1
    print(faces)