# PTA b 1007

import math

def isprime(num):
    chushu = math.sqrt(num)
    for number in range(3, int(chushu)+1, 2):
        if num % number == 0:
            return False
    return True
'''
def isprime(n):
    if n == 1:
        return False
    r = int(math.floor(math.sqrt(n)))
    flag = True
    for i in range(2, r+1):
        if n % i == 0:
            flag = False
            break
    return flag
'''

n = eval(input())
cnt = 0
ip = 3
rl = [i for i in range(3, n+1, 2)]
for i in rl:
    flag = 0
    if isprime(i):
        flag = 1
    if (flag == 1) & (i - ip == 2):
        cnt += 1
    if flag == 1:
        ip = i
print(cnt)
'''primelist = []
for i in range(1, n+1):
    if isprime(i):
        primelist.append(i)
for i in range(len(primelist)-1):
    if primelist[i+1] - primelist[i] == 2:
        cnt += 1
print(cnt)
'''
'''ip = 2

for i in range(1, n+1):
    flag = 0
    if isprime(i):
        flag = 1
    if (flag == 1) & (i - ip == 2):
        cnt += 1
    if flag == 1:
        ip = i
print(cnt)
'''
'''for i in range(1, n+1):
    if isprime(i) & isprime(i+2) & (i+2 <= n):
        cnt += 1
print(cnt)
'''