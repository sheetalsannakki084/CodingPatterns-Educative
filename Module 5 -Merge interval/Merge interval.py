

def solution(num):
    result=[]

    result.append(num[0])


    for i in range(1,len(num)):
        # Compare the second element of the last interval in 'result' with the first element of the current interval
        if result[-1][1]>=num[i][0]:

            result[-1]=[min(result[-1][0],num[i][0]),max(num[i][1],result[-1][1])]

        else:
            result.append(num[i])

    return result

# result[-1] is used to access the last element in the result list. The -1 means "from the end of the list,"

# SIMILAR to insert but here comparing 1st elemnt with othr elemnets .as it in list so result compare list lastelemnt thts y writing as -1
# result([1,3]) [-1][1]=3 last elemnt in list


input=[[1,2],[3,7],[4,6],[6,8]]
obj=solution(input)
print(obj)
