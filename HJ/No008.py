# !/user/bin/env python
# -*- coding:utf-8 -*-
# kiki 210510
# 数据表
import sys
iDict = {}
for line in sys.stdin.readlines():
    num = line.strip().split(' ')
    if len(num) == 1:
        continue
    iKey, iValue = num
    iKey = int(iKey)
    iValue = int(iValue)
    iDict[iKey] = iValue if iKey not in iDict else iDict[iKey] + iValue
for ke in sorted(iDict.keys()):
    print ke, iDict[ke]