
def word_search(grid,word):
    n=len(grid)
    m=len(grid[0])
    for r in range(n):
        for c in range(m):
            if dfs(r,c,0,word,grid):
                return True
    return False

def dfs(r,c,i,word,grid):

    if i== len(word):
        return True


    if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c]!=word[i]:
       return False

    res=grid[r][c]
    grid[r][c]="*"

    for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if dfs(r + rowOffset, c + colOffset, i + 1, word, grid):
            return True

    grid[r][c] = res  # Revert the cell back to its original value
    return False

grid= [['A', 'B', 'C', 'I'],
       ['P', 'U', 'C', 'M'],
       ['I', 'D', 'E', 'R']]


word="ABCCED"

result=word_search(grid,word)

print("found word in input?",result)
