"""
Combination Sum II

"""

class Solution(object):
    def combinationSum2(self, candidates, target):

        answer = []
        candidates.sort()
        n = len(candidates)

        def recurse(index, subArray, curSum):
            if curSum == target:
                answer.append(subArray)
                return

            if index == n or curSum > target:
                return
    
            newIndex = index
            while newIndex < n - 1 and candidates[newIndex] == candidates[newIndex + 1]:
                newIndex += 1

            
            subArray.append(candidates[index])
            recurse(index + 1, subArray[:], curSum + candidates[index])
            subArray.pop()
            recurse(newIndex + 1, subArray[:], curSum)

        recurse(0, [], 0)
        return answer
            
"""
Time Complexity: O(2ⁿ)
Space Complexity: O(n)

"""