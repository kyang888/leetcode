# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number <= 2:
            return number
        cur = 2
        t1 = 1
        t2 = 2
        while cur < number:
            cur += 1
            temp = t1 + t2
            t1 = t2
            t2 = temp
        return t2