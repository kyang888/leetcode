# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        return self.buildTree(pre, 0, len(pre)-1, tin, 0, len(tin)-1)
    
    def buildTree(self, pre, ps, pe, tin, ts, te):
        if ps <= pe:
            val = pre[ps]
            node = TreeNode(val)
            # node_count 记录左子树结点的个数
            node_count = 0
            while val != tin[node_count + ts]:
                node_count += 1
            node.left = self.buildTree(pre, ps+1, ps+node_count, tin, ts, ts+node_count-1)
            node.right = self.buildTree(pre, ps+node_count+1, pe, tin, ts+node_count+1, te)
            return node
        else:
            return None