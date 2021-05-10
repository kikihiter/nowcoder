# !/user/bin/env python
# -*- coding:utf-8 -*-
# kiki 210510
# No010
import sys
s = sys.stdin.readline().strip()
iDict = {}
for le in s:
    if  0<=ord(le)<=127:
        iDict[le] = 1
print len(iDict)