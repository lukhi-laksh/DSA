"""
Count Collisions on a Road

"""

class Solution(object):
    def countCollisions(self, directions):

        collision = 0
        stack = []
        stack.append(directions[0])
        for dir in directions[1:]:
            if stack and stack[-1] == 'R' and dir == 'L':
                collision+=2
                stack.pop()
                dir = 'S'
            elif stack and stack[-1] == 'S' and dir == 'L':
                collision+=1
                dir = 'S'
            while stack and stack[-1] == 'R' and dir == 'S':
                collision+=1
                stack.pop()
            stack.append(dir)
        return collision

"""
Time Complexity: O(n)
Space Complexity: O(n)

"""