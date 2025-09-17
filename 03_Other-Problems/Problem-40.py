class Solution(object):
    def doesAliceWin(self, s):
        total_vowel = 0
        vowels = "aeiou"

        for char in s:
            if char in vowels:
                total_vowel += 1

        return total_vowel != 0