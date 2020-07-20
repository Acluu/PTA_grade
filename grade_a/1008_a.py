# PTA a 1008

numlist = [int(i) for i in input().split()]
elevator = [0]+numlist[1:]
gradient = [elevator[i+1]-elevator[i] for i in range(len(elevator)-1)]
tsum = 0
for i in gradient:
    if i>0:
        tsum += (i*6)
    if i<0:
        tsum += ((-i)*4)
print((len(elevator)-1)*5+tsum)
