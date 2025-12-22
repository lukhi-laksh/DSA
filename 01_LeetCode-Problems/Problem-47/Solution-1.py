"""
Permutation II

"""



class Solution(object):
    def permute(self,nums,index,ans):
        if index==len(nums)-1:
            if nums not in ans:
                ans.append(nums[:])
        for i in range(index,len(nums)):
            nums[i],nums[index]=nums[index],nums[i]
            self.permute(nums,index+1,ans)
            nums[i],nums[index]=nums[index],nums[i]
    def permuteUnique(self, nums):
        ans=[]
        self.permute(nums,0,ans)
        return ans

"""
Time Complexity: O(n · n!)
Space Complexity: O(n)

"""
