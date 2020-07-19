# PTA A 1006

def transsec(tl):
    return tl[0]*60*60+tl[1]*60+tl[2]

M = eval(input())
if M == 1:
    stuid, *timel = input().split()
    print(stuid,stuid)
    exit(0)

unloctime = 24*60*60
loctime = 0
openman = ""
closeman = ""

for i in range(M):
    stuid, *timel = input().split()
    # 处理时间
    intime, outtime = timel[0], timel[1]
    intimes, outtimes = [int(j) for j in intime.split(':')], [int(j) for j in outtime.split(':')]
    intimesec, outtimesec = transsec(intimes), transsec(outtimes)
    if intimesec < unloctime:
        openman = stuid
        unloctime = intimesec
    if outtimesec > loctime:
        closeman = stuid
        loctime = outtimesec

print(openman,closeman)
