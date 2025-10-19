class Solution(object):
    def findLexSmallestString(self, s, a, b):
        from collections import deque

        visited = set()
        queue = deque([s])
        visited.add(s)
        smallest = s

        def add_op(string):
            chars = list(string)
            for i in range(1, len(chars), 2):  # only odd indices
                chars[i] = str((int(chars[i]) + a) % 10)
            return "".join(chars)

        def rotate_op(string):
            b_mod = b % len(string)
            return string[-b_mod:] + string[:-b_mod]

        while queue:
            cur = queue.popleft()
            if cur < smallest:
                smallest = cur

            # Operation 1: Add `a` to digits at odd indices
            added = add_op(cur)
            if added not in visited:
                visited.add(added)
                queue.append(added)

            # Operation 2: Rotate by `b`
            rotated = rotate_op(cur)
            if rotated not in visited:
                visited.add(rotated)
                queue.append(rotated)

        return smallest
