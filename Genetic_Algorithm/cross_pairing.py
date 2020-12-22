import random

class Cross_pairing:
    @classmethod
    #交叉函数且当前最优不参与
    def copulation(self,select,flag):
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