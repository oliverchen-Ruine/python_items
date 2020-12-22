import random
#选择评估函数
def y(x1,x2):
    return 1/(x1*x1+x2*x2+1)
#自适应度最佳选择函数
def Best(c):
    #计算每条染色体的适应值
    Evl={}
    for i in range(len(c)):
        Evl[i]=y(c[i][0],c[i][1])
    #最优值
    Max=max(Evl.values())
    distance=abs(Max-1)
    #是否满足最优解
    if distance<=0.0000001:
        #求得最佳结果
        BEST=c[list(Evl.keys())[list(Evl.values()).index(Max)]]
        print('最近距离为：%f,最优解为：x1=%f,x2=%f'%(distance,BEST[0],BEST[1]))
        return
    else:
        #返回自适应度最佳值和分别求解的评估函数值
        fitness=sum(Evl.values())
        #返回选择结果
        select=choose(fitness,Evl,c)
        #假设交配概率为0.88
        P=0.88
        #返回交叉结果
        select1=list(select.values())
        cross=copulation(select,list(Evl.keys())[list(Evl.values()).index(Max)])
        #更新交配后新选择结果
        Max_index=list(Evl.keys())[list(Evl.values()).index(Max)]
        cross[Max_index]=select1[Max_index]
        #变异概率为0.1
        p=0.1
        #发生变异
        new=change(p,cross)
        Best(new)


#轮盘赌选择函数
def choose(fitness,Evl,c):
    #每条染色体的自适应比
    Evl1={}
    for i in range(len(Evl)):
        Evl1[i]=Evl[i]/fitness
    l=len(Evl)
    #l次选择
    select={}
    chooseC={}
    for j in range(l):
        m=random.random()
        Probability_Total=0
        for k in range(l):
            Probability_Total=Probability_Total+Evl1[j]
            if Probability_Total>=m:
                select[j]=c[k]
                break
            if k==l-1:
                select[j]=c[k]
        chooseC[j]=[random.random()*select[j][0],random.random()*select[j][1]]

    return  chooseC
#交叉函数且当前最优不参与
def copulation(select,flag):
        select.pop(flag)
        select1=list(select.values())
        j=0
        for i in range(int(len(select)/2)):
            c=random.randint(0,1)
            if c==0:
                temp=select1[j+1][1]
                select1[j+1][1]=select1[j][1]
                select1[j][1]=temp
                j+=2
            else:
                j+=2
        return select
#变异发生函数
def change(p,cross):
    for i in range(len(cross)):
        C=random.random()
        if C<p:
            c=random.randint(0,1)
            cross[i][c]=random.random()
    return cross
if __name__=="__main__":
    c1=[random.uniform(-3,3),random.uniform(-3,3)]
    c2=[random.uniform(-3,3),random.uniform(-3,3)]
    c3=[random.uniform(-3,3),random.uniform(-3,3)]
    c4=[random.uniform(-3,3),random.uniform(-3,3)]
    c5=[random.uniform(-3,3),random.uniform(-3,3)]
    c={0:c1,1:c2,2:c3,3:c4,4:c5}
    s=Best(c)

