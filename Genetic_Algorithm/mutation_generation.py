import random

class Mutation_generation:
    @classmethod
    #变异发生函数
    def change(self,p,cross):
        for i in range(len(cross)):
            C=random.random()
            if C<p:
                c=random.randint(0,1)
                cross[i][c]=random.uniform(-3,3)
        return cross