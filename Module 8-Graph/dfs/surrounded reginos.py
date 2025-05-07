def solution(mat):
    row=len(mat)
    col=len(mat[0])

    def dfs(r,c,mat):
        if r>=len(mat) or c>=len(mat[0]) or r<0 or c<0 or mat[r][c]!="O":
            return

        mat[r][c]="*"

        dfs(r+1,c,mat),
        dfs(r,c+1,mat),
        dfs(r-1,c,mat),
        dfs(r,c-1,mat)



    for r in range(row):
        for c in range(col):
            if mat[r][c]=="O" and (r in (0,row-1) or c in (0,col-1)):
                dfs(r,c,mat)
    for r in range(row):
        for c in range(col):
            if mat[r][c] == "O":
                mat[r][c] = "X"

    for r in range(row):
            for c in range(col):
                if mat[r][c]=="*":
                    mat[r][c]="O"


    return mat






grid=[["X","X","X","X"],
      ["X","O","O","X"],
      ["X","x","O","X"],
      ["X","O","X","X"]]

obj=solution(grid)
print(obj)
