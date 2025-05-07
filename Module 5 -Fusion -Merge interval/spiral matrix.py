def solution(mat):
    row=len(mat)
    col=len(mat[0])
    result=[]
    top=0
    bot=row-1
    left=0
    right=col-1

    while left<=right and top<=bot:
        #first row---so here we have to check mat[top][left] to mat[top][right]
        for i in range(left,right+1):
            result.append(mat[top][i])

        top+=1

        #right column from top ot bottm in last column
        # so here we have to check mat[top][right] to mat[bot][right]-we have bot+1 bcz to include bot also we added +1,
        # if we give only bot den it will include last bot value
        for i in range(top,bot+1):
            result.append(mat[i][right])
        right-=1

        #right to left so here its mat[bot][right] to mat[bot][left]
        if top<=bot:
            for i in range(right, left - 1, -1):
                result.append(mat[bot][i])
            bot -= 1


        #bot ot top so here its mat[bot][left] to mat[top][left]
        if left<=right:
            for j in range(bot, top - 1, -1):
                result.append(mat[j][left])
            left += 1



    return result



mat=[
    [1,2,3,0],
    [4,5,6,10],
    [12,13,14,15],
    [7,8,9,11]]
obj=solution(mat)
print(obj)
