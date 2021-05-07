# !/user/bin/env python
# -*- coding:utf-8 -*-
# kiki 20210507
# 1.最后单词的长度
import sys
s = sys.stdin.readline().strip()
"""
头疼，输入输出这么难搞的嘛
"""
ans = 0
for i in range(len(s)-1,-1,-1):
    if s[i] != ' ':
        ans += 1
    else:
        break
print ans