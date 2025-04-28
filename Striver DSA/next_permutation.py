# next permutation brute froce approach

from typing import List 
class Solution:
    def genAllpermutation(self, nums, ans, ds, freq):
        if len(ds)==len(nums):
            ans.append(ds.copy())
            return
        for i in range(len(nums)):
            if not freq[i]:
                # Skip duplicates for lexicographical uniqueness
                if i > 0 and nums[i] == nums[i-1] and not freq[i-1]:
                    continue
                freq[i]=True
                ds.append(nums[i])
                self.genAllpermutation(nums,ans,ds,freq)
                ds.pop()
                freq[i]=False

    def permute(self, nums):
        ans=[]
        ds=[]
        freq=[False]*len(nums)
        self.genAllpermutation(nums,ans,ds,freq)
        ans.sort()
        return ans
        
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ans = self.permute(sorted(nums))
        for i in range(len(ans)):
            if ans[i]==nums:
                if i+1 < len(ans):
                    # Modify nums in-place
                    nums[:] = ans[i+1]
                else:
                    # If current is last, wrap around to first
                    nums[:] = ans[0]
                break
    
def main():
    obj = Solution()
    
    nums = [1, 2, 3]
    print("Original:", nums)
    obj.nextPermutation(nums)
    print("Next permutation:", nums)

main()