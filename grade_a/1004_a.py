# PTA test A 1004

def DFS(node, adjlist, visited, level):
    global depth, senioritylevel
    if depth<level:
        depth = level
    visited[int(node)] = 1
    if node in adjlist:
        nodeadj = adjlist[node]
        for anode in nodeadj:
            if visited[int(anode)] == 0:
                DFS(anode, adjlist, visited, level+1)
    else:
        senioritylevel[level] += 1        
    


# 需求 建个树，输出每一层的叶子节点数量
# N输入0 不返回任何值

# 处理输入 建树
fp = input()
if fp=='0':
    exit(0)
else:
    N, M = [int(i) for i in fp.split()]
adjlist={} # 邻接表
for i in range(M):
    ID, K, *children= input().split()
    K = int(K)
    adjlist[ID] = []+children
# DFS 
# 1. 遍历每个节点 怎么判断层数？调用递归时+1 dfs(node, level+1)
# 2. max(level)即为树的层数，先按最坏情况开array，最后切片
# 3. 判断是不是没有子节点，是的话该层对应+1
level = 0  # 初始层数
senioritylevel = [0]*100  # 最不平衡树 每层一个
depth = 0  # 树深度
visited = [0]*(N+1) # 是否访问，方便起见首位不用

DFS('01', adjlist, visited, level)


# 输出
print(' '.join([str(i) for i in senioritylevel[:depth+1]]))
