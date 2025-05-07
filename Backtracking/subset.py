class solution:
    def backtrack(self,index, path,nums,result):
        if index >= len(nums):
            result.append(path.copy())
            return
        path.append(nums[index])
        self.backtrack(index+1,path,nums,result)
        path.pop()
        self.backtrack(index+1,path,nums,result)

#1st base case which s main thing .den return it back .do frm tree type den its easy to write refre code na debug

    def subset(self,nums):
        result=[]
        self.backtrack(0, [],nums,result)
        return result



nums=[1,2,3]
obj=solution()

print(obj.subset(nums))
