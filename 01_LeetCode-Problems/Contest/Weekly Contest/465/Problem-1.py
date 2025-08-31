class Solution(object):
    def recoverOrder(self, order, friends):
        ans = []
        for i in order:
            if i in friends:
                ans.append(i)
        return ans
    
sol = Solution()
order = [3, 1, 2, 5, 4]
friends= [1, 3, 4]
print(sol.recoverOrder(order, friends))
