from collections import defaultdict


def solution(inf,foll):
    n=len(inf)
    relation=defaultdict(list)
    visited=set()
    count=0
    stack=[]

    for i in range(n):
        if foll[i]!=-1:
            relation[inf[i]]=foll[i]

    def dfs(infi):
        stack.append(infi)
        while stack:
            connection=stack.pop()

            if connection not in visited:
                visited.add(connection)
                if connection in relation:
                    stack.append(relation[connection])


    for infi in inf:
        if infi not in visited:
            dfs(infi)

            count+=1

    return count





# influencers = [2, 1,5, 3, 4]
# followers = [-1, 5, 3, 5, 3]
# influencers= [1, 2, 3]
# followers= [3, 2, 1]
influencers= [2, 1,5, 3, 4]
followers= [-1, 5, 3, 5, 3]
obj=solution(influencers,followers)
print(obj)