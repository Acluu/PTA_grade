# PTA b 1001

def odddid(n):
    return 0.5*(3*n+1)

def evendid(n):
    return 0.5*n

n=eval(input())
count=0
while n!=1:
    if n%2 == 0:
        n = evendid(n)
    else:
        n = odddid(n)
    count+=1
print(count)