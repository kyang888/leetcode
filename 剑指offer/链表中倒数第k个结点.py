# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 前后指针的做法
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

# 递归的做法
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if k == 0:
            return None
        result = [k]
        self.f(head, result)
        if len(result) == 1:
            return None
        else:
            return result[1]

    def f(self, head, result):
        if head:
            self.f(head.next, result)
            result[0] -= 1
            if result[0] == 0:
                result.append(head)
