# PTA test 单源最短路
# 筛选条件 1. least cost 2. max happy 3. max average happy
'''7-4 All Roads Lead to Rome (30分)
Indeed there are many different tourist routes from our city to Rome. You are supposed to find your clients the route with the least cost while gaining the most happiness.

Input Specification:
Each input file contains one test case. For each case, the first line contains 2 positive integers N (2≤N≤200), the number of cities, and K, the total number of routes between pairs of cities; followed by the name of the starting city. The next N−1 lines each gives the name of a city and an integer that represents the happiness one can gain from that city, except the starting city. Then K lines follow, each describes a route between two cities in the format City1 City2 Cost. Here the name of a city is a string of 3 capital English letters, and the destination is always ROM which represents Rome.

Output Specification:
For each test case, we are supposed to find the route with the least cost. If such a route is not unique, the one with the maximum happiness will be recommanded. If such a route is still not unique, then we output the one with the maximum average happiness -- it is guaranteed by the judge that such a solution exists and is unique.

Hence in the first line of output, you must print 4 numbers: the number of different routes with the least cost, the cost, the happiness, and the average happiness (take the integer part only) of the recommanded route. Then in the next line, you are supposed to print the route in the format City1->City2->...->ROM.

Sample Input:
6 7 HZH
ROM 100
PKN 40
GDN 55
PRS 95
BLN 80
ROM GDN 1
BLN ROM 1
HZH PKN 1
PRS ROM 2
BLN HZH 2
PKN GDN 1
HZH PRS 1
Sample Output:
3 3 195 97
HZH->PRS->ROM'''
# 处理输入 建立邻接表
N, K, startpos = input().split()
N = int(N)
K = int(K)
happydic = {}
encode = []
encode.append(startpos)
for i in range(N-1):
    site, hap = input().split()
    hap = int(hap)
    happydic[site] = hap
    encode.append(site)
#adjlist={}  #邻接表怎么体现距离?
# 改用邻接矩阵，邻接矩阵编码按照happydic key 起始点编码即为0
inf=float('inf')
adjmatrix = [[inf]*N for i in range(N)]
for i in range(K):
    s1, s2, cost = input().split()
    cost = int(cost)
    ss1, ss2 = encode.index(s1), encode.index(s2)
    adjmatrix[ss1][ss2]=adjmatrix[ss2][ss1] = cost

# 单源最短路怎么写 dijastraQAQ
route = []
mincost = inf
maxhappy = 0
maxaveragehappy = 0
visited = [1]+[0]*(N-1)
