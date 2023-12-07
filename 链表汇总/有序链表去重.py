# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        a = head
        while a is not None and a.next is not None:
            if a.val == a.next.val:
                a.next = a.next.next
            else:
                a = a.next
        return head

