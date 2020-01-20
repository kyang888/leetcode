# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        # 如果有0,1,2层,则返回0,1,2
        if number <= 2:
            return number
        t1 = 1
        t2 = 2
        # t2表示s个台阶的跳法，t1表示s-1个台阶的跳法
        s = 2
        while s < number:
            s += 1
            temp = t1 + t2
            t1 = t2
            t2 = temp
        return t2