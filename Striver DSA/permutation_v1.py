# calculate permutation

class Solution:
    def recurPermute(self,nums,ds,freq,ans):
        if len(freq)==len(ds):
            ans.append(ds.copy())
            return
        for i in range(len(nums)):
            if freq[i]==False:
                ds.append(nums[i])
                freq[i]=True
                self.recurPermute(nums,ds,freq,ans)
                ds.pop()
                freq[i]=False

    def permute(self,nums):
        ds=[]
        freq=[False]*len(nums)
        ans=[]
        self.recurPermute(nums,ds,freq,ans)
        return ans
    
def main():
    obj=Solution()
    print(obj.permute(nums=[1,2,3]))

main()