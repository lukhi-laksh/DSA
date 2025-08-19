"""
Integer to Roman
"""
class Solution(object):
    def intToRoman(self, num):
        dictt = {
            1: 'I',
            2: 'II',
            3: 'III', 
            4: 'IV',
            5: 'V',
            6: 'VI',
            7: 'VII',
            8: 'VIII',
            9: 'IX',
            10: 'X',
            20: 'XX',
            30: 'XXX',
            40: 'XL',
            50: 'L',
            60: 'LX',
            70: 'LXX',
            80: 'LXXX', 
            90: 'XC',
            100: 'C',
            200: 'CC',
            300: 'CCC',
            400: 'CD',
            500: 'D',
            600: 'DC',
            700: 'DCC',
            800: 'DCCC',
            900: 'CM',
            1000: 'M',
            2000: 'MM',
            3000: 'MMM'
        }

        if num == 0:
            return ""

        nums = str(num)
        first_val = int(nums[0] + '0' * (len(nums) - 1))

        rest_val = int(nums[1:]) if len(nums) > 1 else 0

        return dictt[first_val] + self.intToRoman(rest_val)


sol = Solution()
print(sol.intToRoman(3566))

"""
Time Complexity:  O(d) = O(log n)
Space Complexity: O(d) = O(log n)

"""