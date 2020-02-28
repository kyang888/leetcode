# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent == 0:
            return 1.0
        flag = 1 if exponent > 0 else -1
        if exponent < 0:
            exponent = -exponent
        l = []
        while exponent > 0:
            l.append(exponent % 2)
            exponent = exponent // 2
        l = l[::-1]
        result = base ** l[0]
        for r in l[1:]:
            result = (result ** 2)* (base ** r)
        if flag < 0:
            return 1.0/result
        return result