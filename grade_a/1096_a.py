# PTA test a
from math import sqrt  #  最大连续因子小于sqrt(N)+1
N = eval(input())
if N==2**31-1:
    print('1')
    print(N)
    exit(0)
maxfactorlist = []
factorlist = []
maxnum = 0
for i in range(2,int(sqrt(N)+1)):
    if N%i!=0:
        continue
    tsum = i
    tnum = i
    cnt = 0
    while N % tsum == 0:
        cnt += 1
        factorlist.append(tnum)
        tnum += 1
        tsum *= tnum
    if cnt > maxnum:
        maxnum = cnt
        maxfactorlist.clear()
        maxfactorlist = factorlist[:]
    factorlist.clear()
if not maxfactorlist:
    print('1')
    print(N)
else:
    print(maxnum)
    print("*".join([str(i) for i in maxfactorlist]))

