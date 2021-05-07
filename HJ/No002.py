# !/user/bin/env python
# -*- coding:utf-8 -*-
# kiki 20210507
import sys
s = sys.stdin.readlines()
letter = s[1].strip().lower()
iStr = s[0].strip().lower()
print iStr.count(letter)