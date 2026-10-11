# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        fast = head
        slow = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        prev = None

        while slow is not None:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        left = head
        right = prev

        while right is not None:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True
        