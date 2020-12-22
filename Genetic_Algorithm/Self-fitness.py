import random
import matplotlib.pyplot as plt
import numpy as np

from Genetic_Algorithm import Selective_evaluation
from Genetic_Algorithm import Roulette_selection
from Genetic_Algorithm import cross_pairing
from Genetic_Algorithm import mutation_generation

class Self_fitness:
    def __init__(self):
        print("")
    @classmethod
    #自适应度最佳选择函数
    def Best(self,c,tag):
        if tag==0:
            plt.figure()
            plt.scatter(0,0)
            plt.xlabel('x')
            plt.ylabel('y')
        y=Selective_evaluation.Selective_evaluation
        #计算每条染色体的适应值
        Evl={}
        for i in range(len(c)):
            Evl[i]=y.y(c[i][0],c[i][1])
        #最优值
        Max=max(Evl.values())
        distance=abs(Max-1)
        BEST=c[list(Evl.keys())[list(Evl.values()).index(Max)]]
        plt.scatter(BEST[0],BEST[1])
        plt.annotate(r'$%d$' % tag,xy=(BEST[0],BEST[1]),xycoords='data',xytext=(+30,-30),
             textcoords='offset points',fontsize=7,
             arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))
        print('当前最近距离为：%.10lf,最优解为：x1=%.10lf,x2=%.10lf'%(distance,BEST[0],BEST[1]))
        #是否满足最优解
        if distance<=0.0000001:
            #求得最佳结果
            print('最近距离为：%.10lf,最优解为：x1=%.10lf,x2=%.10lf'%(distance,BEST[0],BEST[1]))
            plt.show()
            return
        else:
            #返回自适应度最佳值和分别求解的评估函数值
            fitness=sum(Evl.values())
            #返回选择结果
            choose=Roulette_selection.Roulette_select
            select=choose.choose(fitness,Evl,c)
            #返回交叉配对结果
            select1=list(select.values())
            copulation=cross_pairing.Cross_pairing
            cross=copulation.copulation(select,list(Evl.keys())[list(Evl.values()).index(Max)])
            #更新交配后新选择结果
            Max_index=list(Evl.keys())[list(Evl.values()).index(Max)]
            cross[Max_index]=select1[Max_index]
            #变异概率为0.1
            p=0.1
            #发生变异
            change=mutation_generation.Mutation_generation
            new=change.change(p,cross)
            tag+=1
            Self_fitness.Best(new,tag)
if __name__=="__main__":
    c1=[random.uniform(-3,3),random.uniform(-3,3)]
    c2=[random.uniform(-3,3),random.uniform(-3,3)]
    c3=[random.uniform(-3,3),random.uniform(-3,3)]
    c4=[random.uniform(-3,3),random.uniform(-3,3)]
    c5=[random.uniform(-3,3),random.uniform(-3,3)]
    c={0:c1,1:c2,2:c3,3:c4,4:c5}
    Self_fitness.Best(c,0)