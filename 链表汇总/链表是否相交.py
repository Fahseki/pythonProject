# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        last = headA

        n = 1
        i = 0

        #  遍历其中一个链表，获得长度，且将其首尾相连转化成环
        while last.next is not None:
            last = last.next
            n += 1
        last.next = headA

        # 转化为，存在环的链表，找环的起点
        slow = headA
        fast = headB
        while fast is not None and fast.next is not None:
            # 当双指针相遇，说明存在环
            if fast == slow:
                # 重新循环双指针，前后拉开环内节点个数的长度，即：链表A的长度
                slow = headB
                fast = headB
                while i < n:
                    fast = fast.next
                    i += 1
                # 双指针再次相遇时，此时即是所求节点
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                last.next = None
                return slow
            else:
                fast = fast.next.next
                slow = slow.next
        last.next = None
        return None

# 尝试写一下双指针法
# 双指针都走了两个链表的长度
# 同时指向空时，说明不相交
    def double_p_node(self, headA, headB):
        if headA is None or headB is None:
            return None
        p_a = headA
        p_b = headB
        while p_a != p_b:
            if p_a is None:
                p_a = headB
            else:
                p_a = p_a.next
            if p_b is None:
                p_b = headA
            else:
                p_b = p_b.next
        return p_a



