# PTA a 1001

n = sum(list(map(int, input().split())))
cnt = 1
out = ''
for i in str(n)[::-1]:
    out = i + out
    if ((cnt%3 == 0) & (cnt+1 < len(str(n)))& (n<0)) | ((cnt%3 == 0) & (cnt < len(str(n))) & (n>0)):
        out=','+out
    cnt += 1
print(out)
