class solution:

    def find(self,nums,t):
        result=[]
        self.solve(0,[],nums,result,0)
        return result


    def solve(self,index,path,nums,result,sum):

        if sum==t:
            result.append(path.copy())
            return True
        if sum>t:
            return False
        if index>=len(nums):
            return False

        sum+=nums[index]
        path.append(nums[index])
        pick=self.solve(index+1,path,nums,result,sum)
        if pick==True:
            return True
        ans=path.pop()
        sum=sum-ans
        self.solve(index + 1, path, nums, result,sum)




nums=[5,1,1,9,2,10]

t=9
obj=solution()
print(obj.find(nums,t))


#code and debug