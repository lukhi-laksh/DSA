"""
Count the numer of Computer Unlocking Permutations

"""

class Solution(object):
    def countPermutations(self, complexity):

        MOD = 1e9 + 7
        if sorted(complexity)[0] != complexity[0]:
            return 0
        if sorted(complexity)[0] == sorted(complexity)[1]:
            return 0
        def factorial(n):
            fact = 1
            for i in range(1,n):
                fact *= i
                fact %= MOD
            return fact
        return int(factorial(len(complexity)))
    

"""
Time Complexity: O(n)
Space Complexity: O(1)

"""