# PTA test supply chain
'''7-3 Highest Price in Supply Chain (25分)
A supply chain is a network of retailers（零售商）, distributors（经销商）, and suppliers（供应商）-- everyone involved in moving a product from supplier to customer.

Starting from one root supplier, everyone on the chain buys products from one's supplier in a price P and sell or distribute them in a price that is r% higher than P. It is assumed that each member in the supply chain has exactly one supplier except the root supplier, and there is no supply cycle.

Now given a supply chain, you are supposed to tell the highest price we can expect from some retailers.

Input Specification:
Each input file contains one test case. For each case, The first line contains three positive numbers: N (≤10
​5
​​ ), the total number of the members in the supply chain (and hence they are numbered from 0 to N−1); P, the price given by the root supplier; and r, the percentage rate of price increment for each distributor or retailer. Then the next line contains N numbers, each number S
​i
​​  is the index of the supplier for the i-th member. S
​root
​​  for the root supplier is defined to be −1. All the numbers in a line are separated by a space.

Output Specification:
For each test case, print in one line the highest price we can expect from some retailers, accurate up to 2 decimal places, and the number of retailers that sell at the highest price. There must be one space between the two numbers. It is guaranteed that the price will not exceed 10
​10
​​ .

Sample Input:
9 1.80 1.00
1 5 4 4 -1 4 5 3 6
Sample Output:
1.85 2'''
# 给定供应链上的node 求最大利润
# 初步想法：dfs 找到最深的level用层数？
# 给了前驱表 遍历一遍看誰最长可否？
# 可能需要剪枝

def findpath(node,level):
    global forwardpath
    if forwardpath[node] == -1:
        return level
    return findpath(forwardpath[node], level+1)



N,p,r = [float(i) for i in input().split()]
N = int(N)
forwardpath = [int(i) for i in input().split()]
maxlevel = 0
seller = 0
for i in range(N):
    thislevel = findpath(i,level = 0)
    if thislevel>maxlevel:
        seller = 1
        maxlevel = thislevel
    elif thislevel == maxlevel:
        seller += 1
price = p * (1+r/100)**maxlevel
print("%.2f %d" %(price, seller))
