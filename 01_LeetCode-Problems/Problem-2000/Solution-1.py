"""
Reverse Prefix of word

"""
class Solution(object):
    def reversePrefix(self, word, ch):
        stack = []
        res = ""
        
        if ch not in word:
            return word
        
        for c in word:
            stack.append(c)
            if c == ch:
                break
        
        a = len(stack) - 1
        
        for i in range(len(word)):
            if stack:
                res += stack.pop()
            elif i > a:
                res += word[i]
        
        return res

"""
Time Complexity:  O(n)
Space Complexity: O(n)

"""