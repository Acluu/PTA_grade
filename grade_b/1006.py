# PTA b 1006

n = eval(input())
cnt = 1
otp = ''
while n > 0:
    presentnum = n % 10
    n = int(n/10)
    if (cnt == 1) & (presentnum == 0):
        cnt += 1
        continue
    if cnt == 1:
        tps = ''
        for i in range(1, presentnum+1):
            tps += str(i)

    elif cnt == 2:
        tps = 'S' * presentnum
    elif cnt == 3:
        tps = 'B' * presentnum
    otp = tps + otp
    cnt += 1
print(otp)
