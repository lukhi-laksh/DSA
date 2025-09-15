"""
Maximum Number of word you can type

"""

class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        
        l = text.split()
        count = 0
        for i in l:
            for j in brokenLetters:
                if j in i:
                    break
            else:
                count += 1
        return count

sol = Solution()
text = 'hello world'
brokenLetters = 'w'
print(sol.canBeTypedWords(text, brokenLetters))

"""
Time Complexity:  O(n * m)
Space Complexity: O(n + b)

"""