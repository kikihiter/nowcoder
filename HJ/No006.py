# !/user/bin/env python
# -8- coding:utf-8 -*-
# 质因数分解
import sys
num = int(sys.stdin.readline().strip())

i = 2
while num != 1 and i*i <= num:
    while num % i == 0 and num != 1:
#         print i,
        sys.stdout.write(str(i)+' ')
        num /= i
    i += 1
if num != 1:
    sys.stdout.write(str(num)+' ')
"""
很烦，会超时
大的素数，很难处理，基本上数字多大就需要多大的循环
最大的是2147483647
       214748373
       13506187 
尝试剪枝也不行啊
"""
"""
终于不超时了，这里有一个剪枝条件需要理解—— i*i <= num
"""