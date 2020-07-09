# PTA 1008 in vscode

n, m = [int(i) for i in input().split()]
m %= n
nlist = [int(i) for i in input().split()]
olist = nlist[-m:]+nlist[:-m]
print(' '.join([str(i) for i in olist]))
