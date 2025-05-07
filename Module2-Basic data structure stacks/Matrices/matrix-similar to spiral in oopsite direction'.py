def solution(mat):

    row=len(mat)
    col=len(mat[0])
    result=[]
    top=0
    left=0
    bot=row-1
    right=col-1

    while left<=right and top<=bot:
        for i in range(top,bot+1):
            result.append(mat[i][left])
        left+=1

        for j in range(left,right+1):
            result.append(mat[bot][j])
        bot-=1

        for i in range(bot,top-1,-1):
            result.append(mat[i][right])
        right-=1


        for j in range(right,left-1,-1):
            result.append(mat[top][j])
        top+=1

    return result







mat = [[1, 2, 3,10],
       [4, 5, 6,11],
       [7, 8, 9,12],
       [13,15,25,22]
       ]


obj = solution(mat)
print(obj)
