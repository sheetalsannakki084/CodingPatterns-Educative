from collections import deque


def solution(mat):
    row=len(mat)
    col=len(mat[0])
    count=0
    fresh=0
    q=deque()
    for r in range(row):
        for c in range(col):
            if mat[r][c]==1:
                fresh+=1
            if mat[r][c]==2:
                q.append([r, c])
    dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    while q and fresh>0:
        for _ in range(len(q)):
            curr, curc = q.popleft()
            for dr, dc in dir:
                newr = curr + dr
                newc = curc + dc
                if (newr in range(row)  and newc in range (col) and
                        mat[newr][newc] == 1):

                    mat[newr][newc] = 2
                    q.append([newr, newc])
                    fresh-=1
        count+=1

    return count if fresh==0 else -1

grid = [[2,1,1],[0,1,1],[1,0,1]]

obj=solution(grid)
print(obj)