
def solution(mat):
    # n =len(mat)
    # for r in range(n//2):
    #     for c in range(r,n-r-1):
    #         mat[r][c],mat[c][n-1-r]=mat[c][n-1-r],mat[r][c]
    #
    #         mat[r][c],mat[n-1-r][n-1-c]=mat[n-1-r][n-1-c],  mat[r][c]
    #
    #         mat[r][c],mat[n-1-c][r]=mat[n-1-c][r],mat[r][c]
    #
    # return mat

    # 1st transpose they did an dden reverse thy did
    row=len(mat)
    col=len(mat[0])

    for i in range(row):
        for j in range(i,col):
            mat[i][j],mat[j][i] =mat[j][i],  mat[i][j]


    for k in range(row):
        l,r=0,col-1
        while l<r:
            mat[k][l],mat[k][r]=mat[k][r], mat[k][l]
            l+=1
            r-=1


    return mat


# both are good but 1st ne code is diff to understanf so second on eis easy
# ex 123,456,789 transpose to 147,258,369 den reverse uisng 2 pointer 741852,963,










mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
obj=solution(mat)
print(obj)