"""
Add Two Numbers
"""

class Solution(object):
    def addTwoNumbers(self, l1, l2):

        carry = 0
        head = None
        tail = None

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            digit = total % 10
            carry = total // 10

            newNode = ListNode(digit) # type: ignore

            if head is None:
                head = newNode
                tail = newNode
            else:
                tail.next = newNode
                tail = newNode

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return head

"""
Time Complexity: O(max(n, m))
Space Complexity: O(max(n, m))

"""