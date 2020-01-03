# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(-1)
        cur = head
        while l1 or l2:
            # 如果l1是None,则拼接l2,break
            if not l1:
                cur.next = l2
                break
            # 如果l1是None,则拼接l2,break
            elif not l2:
                cur.next = l1
                break
            # l1和l2非空,比较l1.val与l2.val
            else:
                if l1.val <= l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
            cur = cur.next
        return head.next