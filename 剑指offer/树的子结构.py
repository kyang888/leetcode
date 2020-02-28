# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot1 and pRoot2:
            return self.f(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right,                                                                                           pRoot2)
        # 如果当前pRoot1 或 pRoot2有一个为空
        else:
            return False
    def f(self, pRoot1, pRoot2):
        # 如果pRoot1还有子结点而当前的pRoot2已为空
        if pRoot1 and not pRoot2:
            return True
        # 如果pRoot1和pRoot2同时为空
        if not pRoot1 and not pRoot2:
            return True
        if not pRoot1 and pRoot2:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.f(pRoot1.left, pRoot2.left) and self.f(pRoot1.right, pRoot2.right)
