import re
pots = set()
"""初始一级点与源点的坐标"""
pots1 = set()
"""所有二级点的坐标"""
pots2 = set()
"""新增点的坐标"""
pots3 = set()
with open('D:/360MoveData/Users/olive/Desktop/data2.txt', 'r') as f:
        for eachline in f:
            tmp = re.split("\s+",eachline.rstrip())
            pots1.add((int(tmp[0]),int(tmp[1])))
with open('D:/360MoveData/Users/olive/Desktop/data3.txt', 'r') as A:
    for eachline in A:
        tmp = re.split("\s+",eachline.rstrip())
        pots2.add((int(tmp[0]),int(tmp[1])))
pots1 = list(map(list,pots1))
pots2 = list(map(list,pots2))
dic=[]
postmin = 100000
for i in range(168):
        for j in range(168):
            if(i!=j):
                pots = list(map(list,pots1))
                pots.append(pots2[i])
                pots.append(pots2[j])
                print(pots)
            else:
                break