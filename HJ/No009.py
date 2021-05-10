# !/user/bin/env python
# -*- coding:utf-8 -*-
# kiki 210510
# No009
import sys
s = sys.stdin.readline().strip()
num = ""
for i in range(len(s)-1, -1, -1):
    if s[i] not in num:
        num += s[i]
print int(num)