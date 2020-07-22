# PTA test a7-1 20
# 读入两个数 输出加减乘除 输出模块检查化为带分数 注意负数
def maxyue(a,b):
    #求两个整数最大公约数
    a=abs(a)
    b=abs(b)
    for t in range(min(a,b),0,-1):
        if (a%t==0)&(b%t==0):
            return t


# 检查分子分母返回输出字符串部分
def check(u,d):
    if u*d < 0:
        isneg = 1
    else:
        isneg = 0
    if d == 0:
        return 'Inf'
    if u == 0:
        return "0"
    u = abs(u)
    d = abs(d)
    sn = maxyue(u, d)
    u = int(u/sn)
    d = int(d/sn)
    if u/d < 1:
        if isneg == 0:
            return str(u)+'/'+str(d)
        else:
            return f"(-{u}/{d})"
    else:
        sn = maxyue(u,d)
        nu = int(abs(u/sn))
        nd = int(abs(d/sn))
        z = 0 # 带分数整数部分 为0不输出
        while nu>=nd:
            nu -= nd
            z += 1
        if (nu==0) & (isneg==1):
            return f"(-{z})"
        elif (nu==0) & (isneg==0):
            return f"{z}"
        elif isneg == 1:
            return f"(-{z} {nu}/{nd})"
        else:
            return f"{z} {nu}/{nd}"



# 处理输入
n1, n2 = [i for i in input().split()]
n1u, n1d = [int(i) for i in n1.split('/')]
n2u, n2d = [int(i) for i in n2.split('/')]

tsumu = n1u*n2d+n2u*n1d
tsumd = n1d*n2d
tminu = n1u*n2d-n2u*n1d
tmind = n1d*n2d
tprou = n1u*n2u
tprod = n1d*n2d
tchuu = n1u*n2d
tchud = n2u*n1d
print(check(n1u,n1d),'+',check(n2u,n2d),'=',check(tsumu,tsumd))
print(check(n1u,n1d),'-',check(n2u,n2d),'=',check(tminu,tmind))
print(check(n1u,n1d),'*',check(n2u,n2d),'=',check(tprou,tprod))
print(check(n1u,n1d),'/',check(n2u,n2d),'=',check(tchuu,tchud))

