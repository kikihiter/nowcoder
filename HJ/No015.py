num = input()
n = 0
while num != 0:
    num = num&(num-1)
    n += 1
print n