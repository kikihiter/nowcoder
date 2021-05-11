# !/user/bin/env python
# -*- coding:utf-8 -*-
# kiki 210510
# 重构判断语句的排序问题
import sys
nums = sys.stdin.readlines()
nums = nums[1:]
nums = sorted(nums)
for num in nums:
    print num.strip()
"""
偷懒了，直接sorted就行了
"""