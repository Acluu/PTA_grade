# PTA b 1002

numdic = ['ling','yi','er','san','si','wu','liu','qi','ba','jiu']
n = [int(i) for i in list(input())]
s = list(map(int,list(str(sum(n)))))
out=''
for i in s:
    out+=numdic[i]+' '

print(out.strip())
