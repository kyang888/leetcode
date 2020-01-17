# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        rows = len(array)
        # 当前
        if rows == 0:
            return False
        cols = len(array[0])
        row = 0
        col = len(array[0]) - 1
        while col > -1 and row < rows:
            if target < array[row][col]:
                col -= 1
                continue
            if target == array[row][col]:
                return True
            if target > array[row][col]:
                while row < rows:
                    if array[row][col] < target:
                        row += 1
                        continue
                    if array[row][col] == target:
                        return True
                    if array[row][col] > target:
                        col -= 1
                        break
        return False