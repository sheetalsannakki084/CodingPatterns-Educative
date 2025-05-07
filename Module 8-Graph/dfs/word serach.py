

def cal(mat,w):
    row = len(mat)
    col = len(mat[0])
    for r in range(row):
        for c in range(col):
            if backtrack(r, c, 0, w, mat):
                return True
    return False

def backtrack(r, c, i, w, mat):
    if i == len(w):
        return True

    if r < 0 or c < 0 or r >= len(mat) or c >= len(mat[0]) or mat[r][c] != w[i]:
        return False

    res = mat[r][c]
    mat[r][c] = "*"

    # if backtrack(r, c + 1, i + 1, w,mat):
    #     return True
    # if backtrack(r, c-1, i + 1, w, mat):
    #     return True
    # if backtrack(r+1, c, i + 1, w, mat):
    #     return True
    # if backtrack(r-1, c, i + 1, w, mat):
    #     return True
    if (backtrack(r, c + 1, i + 1, w,mat) or
       backtrack(r, c - 1, i + 1, w, mat) or
       backtrack(r + 1, c, i + 1, w, mat) or
       backtrack(r - 1, c, i + 1, w, mat)):
       return True





    #
    # dir=[(0,1),(1,0),(-1,0),(0,-1)]
    # for rowset,colset in dir:
    #     if backtrack(r+rowset,c+colset,i+1,w,mat):
    #         return True

    mat[r][c]=res
    return False
#
mat=[['E','D','X','I','W'],
     ['P','U','F','M','Q'],
     ['I','C','A','T','E'],
     ['M','A','L','C','A'],
     ['J','T','I','V','E']]
#
# mat=[['E','D','X'],
#      ['I','C','A'],
#      ['J','T','I']]
word="EDUCATIVE"
obj=cal(mat,word)
print(obj)
