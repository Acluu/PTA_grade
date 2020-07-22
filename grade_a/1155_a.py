# PTA a 1155
# 遍历二叉树路径 利用递归、回溯及时pop维护路径

def dfs(index):
    global possheap,N
    if ((index*2>N) & (index*2+1>N)):
        if index <= N:
            for i in range(len(path)-1):
                print(f"{path[i]} ", end="")
            print(path[-1])
    else:
        if index*2+1 <= N:
            path.append(possheap[2 * index + 1])
            dfs(index * 2 + 1)
            path.pop()
        path.append(possheap[2 * index])
        dfs(index * 2)
        path.pop()


N = eval(input())
possheap = [-1]+[int(i) for i in input().split()]
path = []
path.append(possheap[1])
dfs(1)
ismin = ismax = 1
for i in range(2,N+1):
    if possheap[int(i/2)]<possheap[i]:
        ismax = 0
    if possheap[int(i/2)]>possheap[i]:
        ismin = 0
if ismin == 1:
    print("Min Heap")
elif ismax == 1:
    print("Max Heap")
else:
    print("Not Heap")
