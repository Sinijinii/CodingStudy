T = int(input())
for tc in range(T):
    N = int(input())
    score = list(input().split())
    di = set(score)
    li = []
    filtered_score = [s for s in score if score.count(s) >= 6]
    for i in di:
        if score.count(i)>=6:
            li.append(i)

    dic = {}
    sco = {}
    sc = None
    sc2 = None
    res = None
    # print(li)
    for j in li:
        dic[j] = list(filter(lambda x: filtered_score[x] == j, range(len(filtered_score))))
        dic[j] = [idx + 1 for idx in dic[j]]
        # print(dic)
        # print("sc: ",sc, "지금: ",sum(dic[j][:4]))
        # print(dic[j])
        # print("sc2: ",sc2, "지금sc2: ",dic[j][4],"res는? ",res)
        if sc == None:
            sc = sum(dic[j][:4])
            sc2 = dic[j][4]
            res = j
        if sc > sum(dic[j][:4]):
            sc = sum(dic[j][:4])
            res = j
            sc2 = dic[j][4]
        if sc == sum(dic[j][:4]):
            if sc2 > dic[j][4]:
                sc2 = dic[j][4]
                res = j
            # if sc2 > dic[j][4]:
            #     sc2 = dic[j][4]
            #     res = j
                
    print(res)

    # for sc in range(len(dic)):
        