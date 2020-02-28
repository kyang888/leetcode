# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        if not array:
            return array
        #记录数组中第一个偶数的位置
        t = -1
        for i in range(len(array)):
            # 如果当前是偶数且t == -1,说明当前的数字是第一个偶数，记录下来
            if array[i] % 2 == 0 and t == -1:
                t = i
                continue
            # 如果当前是奇数且t > -1， 说明前面已经有偶数，将当前奇数移动到第一个偶数的前面
            if array[i] % 2 == 1 and t != -1:
                while i > t:
                    array[i-1], array[i] = array[i], array[i-1]
                    i = i - 1
                t += 1
        return array
