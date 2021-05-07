# !/user/bin/env python
# -*- coding:utf-8 -*-
# kiki 210507
# 问卷调查，计数排序
import sys
nums = sys.stdin.readlines()
n = int(nums[0].strip())
temp = [0]*1001
ans = []
for i in range(1,len(nums)):
    num = int(nums[i].strip())
    if n > 0:
        n -= 1
    else:
        n = num
        ans.append(temp)
        temp = [0]*1001
        continue
    temp[num] = 1
else:
    ans.append(temp)
for ansList in ans:
    for i in range(1001):
        if ansList[i] != 0:
            print i
