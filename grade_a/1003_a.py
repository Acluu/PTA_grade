# PTA a 1003
# 图 所有最短路算法
# 也不太行- -

# input
N, M, sta, des = [int(i) for i in input().split()]
weight = [int(i) for i in input().split()]
graph = [[float('inf') for k in range(N)] for i in range(N)]

for i in range(M):
    ap, bp, length = [int(i) for i in input().split()]
    graph[ap][bp] = graph[bp][ap] = length

dist = [float('inf') for k in range(N)]  # 当前最短路
dist[sta] = 0
collect = [0 for i in range(N)]
collect[sta] = 1
w = [0 for i in range(N)]
w[sta] = weight[sta]
num = [0 for i in range(N)]
num[sta] = 1
for i in range(N):
    u = -1
    minn = float('inf')
    for j in range(N):
        if (collect[j] == 0) & (dist[j] < minn):
            u = j
            minn = dist[j]
    if u == -1:
        break
    collect[u] = 1
    for v in range(N):
        if (collect[v] == 0) & (graph[u][v] < float('inf')):
            if dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]
                num[v] = num[u]
                w[v] = w[u] + weight[v]
            elif dist[u] + graph[u][v] == dist[v]:
                num[v] += num[u]
                if w[u] + weight[v] > w[v]:
                    w[v] = w[u] + weight[v]

print(num[des], w[des])