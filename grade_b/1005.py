# PTA b 1005


def add(ini, vic, al):
    for i in al:
        if i[0] == ini:
            i.append(int(vic))



n = eval(input())
nums = sorted(list(map(int, input().split())), reverse=True)
adjl = [[nums[i]] for i in range(n)]

for i in nums:
    ci = i
    while ci != 1:
        if ci % 2 == 0:
            ci = int(ci/2)
            if ci in nums:
                add(i, ci, adjl)
        else:
            ci = int((ci * 3 + 1)/2)
            if ci in nums:
                add(i, ci, adjl)
out = ''
for i in adjl:
    cnt = 0
    for j in adjl:
        if i[0] in j:
            cnt += 1
    if cnt == 1:
        out = out+str(i[0])+' '
print(out.strip())

