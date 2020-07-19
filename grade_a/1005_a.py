# PTA test A 1005

spelldic = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',0:'zero'}
N = [int(i) for i in list(input())]
sume = str(sum(N))
opt=''
for i in range(len(sume)):
    opt = opt + spelldic[int(sume[i])] + ' '
print(opt.strip())
