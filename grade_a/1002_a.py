# PTA a 1002


def prepro(inp):
    pol = inp[1:]
    dic = []
    for i in range(int(len(pol)/2)):
        dic.append([pol[2*i], 0.0+pol[2*i+1]])
    return dic


in1 = list(map(eval, input().split()))
in2 = list(map(eval, input().split()))
dic1 = sorted(prepro(in1), reverse=True)
dic2 = sorted(prepro(in2), reverse=True)
dic=[]
while (dic1 != []) & (dic2 != []):
    maxpol = max(dic1[0][0], dic2[0][0])
    tsum = 0
    if maxpol == dic1[0][0]:
        tsum += dic1[0][1]
        dic1.pop(0)
    if maxpol == dic2[0][0]:
        tsum += dic2[0][1]
        dic2.pop(0)
    dic.append([maxpol, tsum])
dic = dic + dic1 + dic2
out = ''
cnt = 0
for i in dic:
    if i[1] != 0:
        cnt += 1
        out = out + ' '+str(i[0])+' '+'%.1f' % (i[1])
out = str(cnt)+out
print(out.strip())
