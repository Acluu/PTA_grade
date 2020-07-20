# PTA test a 1152
from math import sqrt


def isprime(n):
    if (n == 0) | (n == 1):
        return False
    if n == 2:
        return True
    for i in range(2,int(sqrt(n))):
        if n % i == 0:
            return False
    return True


L, K = [int(i) for i in input().split()]
num = input()
outp = 404
for i in range(len(num)-K+1):
    tnum = int(num[i:i+K])
    if isprime(tnum):
        outp = num[i:i+K]
        break
print(outp)

