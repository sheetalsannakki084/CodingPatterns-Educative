import collections


def validanagram(s1,s2):

    table=collections.Counter(s1)


    for i in s2:
        if i in table:
            table[i]-=1
        else:
            return False


    for count  in table.values():
        if count!=0:
            return False

    return True









str1="heart"
str2="earth"
result=validanagram(str1,str2)
print("is it valid anagram",result)