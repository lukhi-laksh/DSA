"""
Relative Sort Array

"""

class Solution:
    def relativeSortArray(self, arr1, arr2):
        sorted_lst = []

        for x in arr2:
            while x in arr1:
                sorted_lst.append(x)
                arr1.remove(x)

        return(sorted_lst+sorted(arr1))

"""
Time Complexity:  O(n)
Space Complexity: O(n)

"""