"""
String Compression

"""


from itertools import groupby

class Solution:
    def compress(self, chars):
        write = 0
        for ch, group in groupby(chars):
            count = len(list(group))
            chars[write] = ch
            write += 1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
        return write

"""
Time Complexity: O(n)
Space Complexity: O(1)

"""