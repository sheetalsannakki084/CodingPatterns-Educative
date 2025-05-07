def solution(mat,sr,sc,color):
    row=len(mat)
    col=len(mat[0])
    count=0

    def dfs(r,c,mat,oldcolor):
        if   r>=len(mat) or c>=len(mat[0]) or r<0 or c<0 or mat[r][c]!=oldcolor:
            return


        # dir=[0,1],[1,0],[-1,0],[0-1]
        # for dr,dc in dir:
        mat[r][c]=color
        if( dfs(r,c+1,mat,oldcolor),
            dfs(r+1, c,mat,oldcolor),
            dfs(r-1,c,mat,oldcolor),
            dfs(r,c-1,mat,oldcolor)):
            return True


    for r in range(row):
        for c in range(col):
            if r==sr and c==sc:

                dfs(r,c,mat,mat[sr][sc])

    return mat

grid = [[1,1,1],[1,1,0],[1,0,1]]
sr=1
sc=1
color=2

obj=solution(grid,sr,sc,color)
print("number of islands",obj)