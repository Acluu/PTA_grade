# PTA b 1003

def istrue(sl):
    sss = set(['A'])
    ppos = sl.index('P')
    tpos = sl.index('T')
    head = sl[:ppos]
    body = sl[ppos:tpos+1]
    end = sl[tpos+1:]

    if (head == end) & (set(head).issubset(sss)) & (body == ['P', 'A', 'T']):
        print('YES')
        return 0
    compare = head+['P','A','T']+head
    cnt = 2
    while len(compare) <= len(sl):
        if compare == sl:
            print('YES')
            return 0
        else:
            compare = head + ['P'] + ['A' for i in range(cnt)]+['T']+head * cnt
        cnt+=1
    print('NO')
    return 0


n = eval(input())
ss = set(['P', 'A', 'T'])
for i in range(n):
    s = input()
    if set(s) == ss:
        slist = list(s)
        istrue(slist)
    else:
        print('NO')