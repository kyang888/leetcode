# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # 如果k<=0,return None
        if k <= 0:
            return None
        first = head
        end = head
        i = 1
        while i < k and first:
            first = first.next
            i += 1
        # first等于None,说明k大于链表长度
        if not first:
            return None
        while first.next:
            first = first.next
            end = end.next
        return end 