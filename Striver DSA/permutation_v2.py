# calculate permutation optimal approach

class Solution:
    def recurPermute(self,index,nums,ans):
        if index==len(nums): #base case
            ans.append(nums.copy())
            return
        for i in range(index, len(nums)):
            self.swap(index,i,nums)
            self.recurPermute(index+1,nums,ans)
            self.swap(index,i,nums)

    def swap(self,index,i,nums):
        nums[i],nums[index]=nums[index],nums[i]

    def permute(self,nums):
        ans=[]
        self.recurPermute(0,nums,ans)
        return ans
    
def main():
    obj=Solution()
    print(obj.permute(nums=[1,2,3]))

main()