# !/user/bin/env python
# -*- coding:utf-8 -*-
# 进制转换
import sys
for line in sys.stdin.readlines():
    line = line.strip().lower()
    num = 0
    for i in range(2,len(line)):
#         if line[i] == 'x':
#             print str(num)
#             break
        temp = 0
        if line[i] == 'a':
            temp = 10
        elif line[i] == 'b':
            temp = 11
        elif line[i] == 'c':
            temp = 12
        elif line[i] == 'd':
            temp = 13
        elif line[i] == 'e':
            temp = 14
        elif line[i] == 'f':
            temp = 15
        else:
            temp = int(line[i])
        num = num*16 + temp
    
    print num