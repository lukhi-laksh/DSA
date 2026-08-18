"""
Find the Larget Almost Missing Integer

"""

class Solution(object):
    def largestInteger(self, nums, k):
        d={};
        for i in nums:
            if(i in d):
                d[i]+=1;
            else:
                d[i]=1;
        if(k==1):
            res=-1;
            for i in d:
                if(d[i]==1):
                    res=max(res,i);
            return res
        elif(k==len(nums)):
            return max(nums);
        else:
            if(d[nums[0]]==1 and d[nums[-1]]==1):
                return max(nums[0],nums[-1]);
            elif(d[nums[0]]==1):
                return nums[0];
            elif(d[nums[-1]]==1):
                return nums[-1];
            else:
                return -1

"""
Time Complexity: O(n)
Space Complexity: O(n)

"""