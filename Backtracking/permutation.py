class solution:

    def permutation(self,n):
        result=[]
        # strl=list(str)
        self.backtrack(n,[],result)
        return result


    def backtrack(self,n,path,result):
        if len(path)==len(n):
            result.append(path.copy())     #just1,2,3 to 123 o=as output
            # result.append("".join(path)) if string sinput abc den abc,acb as ouput insted of a,b,c
            return



        for nums in n:
            if nums not in path:
                path.append(nums)
                self.backtrack(n,path,result)
                path.pop()


#here 1,2,3 is converted to string den print as "123',"132"
#if u wnat o "abc" as "abc','acb' as just write join

n=[1,2,3]
obj=solution()
print(obj.permutation(n))



