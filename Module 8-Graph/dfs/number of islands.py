def solution(mat):
    row=len(mat)
    col=len(mat[0])
    count=0

    def dfs(r,c,mat):
        if   r>=len(mat) or c>=len(mat[0]) or r<0 or c<0 or mat[r][c]!='1':
            return


        # dir=[0,1],[1,0],[-1,0],[0-1]
        # for dr,dc in dir:
        mat[r][c]="*"
        if( dfs(r,c+1,mat),
            dfs(r+1, c,mat),
            dfs(r-1,c,mat),
            dfs(r,c-1,mat)):
            return True


    for r in range(row):
        for c in range(col):
            if mat[r][c]=='1':
                count+=1
                dfs(r,c,mat)

    return count

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]]

obj=solution(grid)
print("number of islands",obj)