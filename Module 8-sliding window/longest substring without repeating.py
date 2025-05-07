
def solution(str):
    maxlen=0
    charset=set()

    l=0


    for r in range(len(str)):
        while str[r] in charset:  #here chekc if its dr den remove l if lsamem sa r den ok othresiwe remove till r nt in list
            charset.remove(str[l])
            l+=1


        charset.add(str[r])
        maxlen=max(maxlen,r-l+1)

    return maxlen













str="pwwkew"
obj=solution(str)
print(obj)