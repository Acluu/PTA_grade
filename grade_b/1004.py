# PTA b 1004
n = eval(input())
ss = []
for i in range(n):
    ss.append(input().split())
    ss[-1][-1] = int(ss[-1][-1])
ss.sort(key=lambda x:x[2],reverse=True)
print(ss[0][0],ss[0][1])
print(ss[-1][0],ss[-1][1])