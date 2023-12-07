# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head

        slow = head

        while head is not None and head.val == val:
            head = head.next

        fast = head.next

        while slow.next is not None:
            if slow.next.val == val:
                slow.next = slow.next.next
            else:
                slow = slow.next
        return head
