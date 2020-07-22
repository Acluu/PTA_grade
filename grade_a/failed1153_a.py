# PAT a 1153
# python太慢了 考虑一下Cpp

# 需求1: 打印给定级别考生成绩 成绩降序排列 成绩相同者按考号字典序升序
def need1(case, par):
    global studentdic, N, M
    backstudentdic = studentdic[:]
    newdic = []
    for i in range(N):
        if backstudentdic[i][1] == par:
            newdic.append(backstudentdic[i])
    outdic = sorted(newdic, key= lambda x: x[5], reverse=True)
    if not outdic:
        print(f'Case {case + 1}: 1 {par}')
        print('NA')
        return 0
    for i in range(len(outdic)-1):
        for j in range(i,len(outdic)):
            if (outdic[i][-1]==outdic[j][-1]) & (outdic[i][0]>outdic[j][0]):
                outdic[i], outdic[j] = outdic[j], outdic[i]
    print(f'Case {case+1}: 1 {par}')
    for i in outdic:
        print(i[0], i[-1])
    return 0


# 需求2: 给定考场 打印总人数和总成绩
def need2(case, par):
    global studentdic, N, M
    backstudentdic = studentdic[:]
    newdic = []
    tsum = 0
    for i in range(N):
        if backstudentdic[i][2] == par:
            newdic.append(backstudentdic[i])
            tsum += backstudentdic[i][-1]
    print(f'Case {case+1}: 2 {par}')
    if len(newdic) == 0:
        print('NA')
        return 0
    print(len(newdic), tsum)
    return 0

# 需求3: 给定日期 打印各个考场考试人数 人数降序 考场升序
def need3(case, par):
    global studentdic, N, M
    backstudentdic = studentdic[:]
    sitedic={}
    for i in range(N):
        if backstudentdic[i][3] == par:
            if backstudentdic[i][2] in sitedic:
                sitedic[backstudentdic[i][2]] += 1
            else:
                sitedic[backstudentdic[i][2]] = 1

    outdic = sorted(sitedic.items(), key=lambda x: x[1], reverse=True)
    if not outdic:
        print(f'Case {case + 1}: 3 {par}')
        print('NA')
        return 0
    for i in range(len(outdic)-1):
        for j in range(i, len(outdic)):
            if (outdic[i][-1] == outdic[j][-1]) & (outdic[i][0] > outdic[j][0]):
                outdic[i], outdic[j] = outdic[j], outdic[i]
    print(f'Case {case+1}: 3 {par}')
    for i in outdic:
        print(i[0], i[-1])
    return 0


N, M = [int(i) for i in input().split()]
studentdic = []  # B 123 180908 127  级别 考场 日期 考号:成绩
for i in range(N):
    cardid, score = input().split()
    score = int(score)
    studentdic.append([cardid, cardid[0], cardid[1:4], cardid[4:10], cardid[10:], score])

for i in range(M):
    typ, par = input().split()
    if typ == '1':
        need1(i, par)
    if typ == '2':
        need2(i, par)
    if typ == '3':
        need3(i, par)
