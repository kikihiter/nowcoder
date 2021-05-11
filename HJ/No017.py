# !/user/bin/env python
# -*- coding:utf-8 -*-
# kiki 210511
# 坐标移动
import sys
s = sys.stdin.readline().strip().split(';')
X = 0
Y = 0
for iStr in s:
    iStr = iStr.strip()
    if not iStr or len(iStr)>3 or len(iStr)<2:
        continue
    try:
        move = int(iStr[1:])
    except:
        continue
    if iStr[0] == 'A':
        X -= move
    elif iStr[0] == 'D':
        X += move
    elif iStr[0] == 'W':
        Y += move
    elif iStr[0] == 'S':
        Y -= move
sys.stdout.write(str(X)+','+str(Y))