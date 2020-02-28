# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        head = ListNode(-1)
        cur = head
        while pHead1 or pHead2:
            # pHead1为空， 直接链接pHead2
            if not pHead1 and pHead2:
                cur.next = pHead2
                pHead2 = pHead2.next
            # pHead2为空，直接链接pHead1
            elif pHead1 and not pHead2:
                cur.next = pHead1
                pHead1 = pHead1.next
            # pHead1和pHead2都非空
            elif pHead1.val <= pHead2.val:
                cur.next = pHead1
                pHead1 = pHead1.next
            else:
                cur.next = pHead2
                pHead2 = pHead2.next
            cur = cur.next
        return head.next