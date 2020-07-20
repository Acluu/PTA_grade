# PTA test a 1009
# 字典排序 格式化输出


eq1 = [float(i) for i in input().split()]
eq2 = [float(i) for i in input().split()]
k1 = int(eq1[0])
k2 = int(eq2[0])
eq1, eq2 = eq1[1:], eq2[1:]
equ1, equ2 = [], []

for i in range(k1):
    equ1.append([int(eq1[2*i]), eq1[2*i+1]])

for i in range(k2):
    equ2.append([int(eq2[2*i]), eq2[2*i+1]])

explist = {}

for ele1 in equ1:
    for ele2 in equ2:
        tele = [ele1[0]+ele2[0], ele1[1]*ele2[1]]
        if tele[0] in explist:
            explist[tele[0]] += tele[1]
        else:
            explist[tele[0]] = tele[1]
sort_exp = sorted(explist.items(), key=lambda d: d[0], reverse=True)
new_sort=[]
for i in sort_exp:
    if i[1] != 0:
        new_sort.append(i)
outp = str(len(new_sort))+' '
for i in new_sort:
    outp += str(i[0]) +' ' +"{:.1f}".format(i[1])+' '
print(outp.strip())
