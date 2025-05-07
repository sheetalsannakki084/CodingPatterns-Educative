

def solution(str):
    prefix=str[0]


    rem=str[1:]

    for st in rem:
        while not  st.startswith(prefix):
            prefix=prefix[:-1]
        if prefix is None:
            return ""


    return prefix
















str=["flower","flow","flight"]
obj=solution(str)
print(obj)