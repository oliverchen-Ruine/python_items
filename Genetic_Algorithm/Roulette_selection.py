import random

class Roulette_select:
    @classmethod
    #轮盘赌选择函数
    def choose(self,fitness,Evl,c):
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
