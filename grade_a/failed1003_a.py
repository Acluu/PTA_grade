# PTA a 1003
# 图 所有最短路算法


# 找到最小的那些邻接未收录点

def FindMinDist(g, d, c):
    global N
    V = []
    min_dist = float('inf')
    for i in range(N):
        if (c[i] == 0) & (d[i] < min_dist):
            V.clear()
            V.append(i)
        if (d[i] < float('inf')) & (d[i] == min_dist):
            V.append(i)
    print(V)
    return V


def save_path(s, e, stack=[]):
    global diffpath, pre, des
    stack.append(e)
    if s == e:
        diffpath.append(stack[::-1])
        stack.clear()
        stack.append(des)
        return 0
    for i in range(len(pre[e])):
        save_path(s, pre[e][i], stack)





def getpathnum(s, e, pre):  #几条最短路？
    if s == e:
        return 1
    count = 0
    for i in range(len(pre[e])):
        count += getpathnum(s, pre[e][i], pre)
    return count

# input
N, M, sta, des = [int(i) for i in input().split()]
teamnum = [int(i) for i in input().split()]
graph = [[float('inf') for k in range(N)] for i in range(N)]
for i in range(N):
    graph[i][i] = 0

for i in range(M):
    ap, bp, length = [int(i) for i in input().split()]
    graph[ap][bp] = graph[bp][ap] = length

# dijkstra
dist = graph[sta]  # 当前最短路
dist[sta] = 0
collect = [0 for i in range(N)]
collect[sta] = 1
pre = [[] for i in range(N)]  # 前驱节点数组
for i in range(N):
    pre[i].append(sta)
pre[sta].clear()
pre[sta].append(-1)
for i in range(N-1):
    mindist = float('inf')
    for w in range(N):
        if (collect[w] == 0) & (dist[w] < mindist):
            v = w
            mindist = dist[w]
    collect[v] = 1
    for w in range(N):
        if (collect[w] == 0) & (mindist + graph[v][w] < dist[w]):
            dist[w] = mindist + graph[v][w]
            pre[w].clear()
            pre[w].append(v)
        if (collect[w] == 0) & (mindist + graph[v][w] == dist[w]) & (v not in pre[w]):
            dist[w] = mindist + graph[v][w]
            pre[w].append(v)

diffpath = []
save_path(sta, des)
teamsum = maxteam = 0
for i in diffpath:
    for j in i:
        teamsum += teamnum[j]
    if maxteam < teamsum:
        maxteam = teamsum
    teamsum = 0
print(getpathnum(sta, des, pre),maxteam)
'''while 1:
    V = FindMinDist(graph, dist, collect)  # 找未收集节点中dist最小的那些
    if not V:
        break
    for i in V:   # 逐一收录
        collect[i] = 1
        for j in range(N):
            if (collect[j] == 0) & (graph[i][j]<float('inf')):
                if dist[i]+graph[i][j] < dist[j]:
                    dist[j] = dist[i]+graph[i][j]
                    pre[j].append(i)
for i in pre:
    print(i)
print()
print(dist)
'''