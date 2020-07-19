# PTA a 1007

# dynamic programing
def finddp(numlist,dp,i):
    if i == 0:
        return numlist[0]
    return max(numlist[i],dp[i-1]+numlist[i])


K = eval(input())
numlist = [int(i) for i in input().split()]

if max(numlist)<0:
    print(0,numlist[0],numlist[-1])
    exit(0)
if max(numlist)==0:
    print(0,0,0)
    exit(0)


startpos = 0
endpos = 0
maxsum = numlist[0]
dp = [0]*K  # 以i为结尾的最大子列和，必须包含i

for i in range(K):
    dp[i] = finddp(numlist,dp,i)
    if dp[i] > maxsum:
        endpos = i
        maxsum = dp[i]
tsum = 0
startpos = endpos
while tsum < maxsum:
    tsum += numlist[startpos]
    startpos -= 1

print(maxsum,numlist[startpos+1],numlist[endpos])
