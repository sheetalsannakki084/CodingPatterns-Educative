

def solution(mat):
    row = len(mat)
    col = len(mat)
    frow = False
    fcol = False
    for i  in range(row):
        if mat[i][0]==0:
            frow=True
    for j in range(col):
        if mat[0][j] == 0:
            fcol = True

    for i in range(1,row):
        for j in range(1,col):
            if mat[i][j]==0:
                mat[i][0]=0
                mat[0][j]=0

    for i in range(1,row):
        if mat[i][0]==0:
            for j in range(1,col):
                mat[i][j]=0

    for j in range(1,col):
        if mat[0][j]==0:
            for i in range(1,row):
                mat[i][j]=0

    if frow:
        for j in range(col):
            mat[0][j]=0
    if fcol:
        for i in range(row):
            mat[i][0]=0

    return mat





mat=[[1, 1, 1],[1, 0, 1],[1, 1, 1]]
obj=solution(mat)
print(obj)
