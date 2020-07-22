# PTA a 1154
# 图的遍历 建个邻接表然后dfs遍历图 看邻接的边是不是一个颜色
# 注意有不连通的点
# 以上内容纯属fp
'''
# dfs

def dfs(index):
    global adjlist, colormap, visited, N, M, K, isKcolor
    visited[index] = 1
    thislist = adjlist[index][1:]
    thiscolor = colormap[index]
    for i in range(len(thislist)):
        if visited[thislist[i]] == 1:
            continue
        if thiscolor != colormap[thislist[i]]:
            dfs(thislist[i])
        else:
            isKcolor = 0
            return 0
    return 0


'''
# 读入数据 顺便建表
N, M = [int(i) for i in input().split()]
adjlist = [] # 存放边的信息
for i in range(M):
    v1, v2 = [int(j) for j in input().split()]
    adjlist.append([v1, v2])

K = eval(input())
for i in range(K):
    colormap = [int(j) for j in input().split()]
    isKcolor = 1
    for edge in adjlist:
        if colormap[edge[0]] == colormap[edge[1]]:
            isKcolor = 0
            break
    if isKcolor == 0:
        print('No')
    else:
        print(f'{len(set(colormap))}-coloring')

