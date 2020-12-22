import matplotlib.pyplot as plt

class Show :
    @classmethod
    def show(self,a,b,c):
        fig=plt.figure()
        ax = fig.add_subplot(111)
        pgon = plt.Polygon((a,b,c), color ='g', alpha = 0.5 )
        ax.add_patch(pgon)
        plt.plot()
        plt.title('The current coordinates')
        plt.show()
        f=open('./show.txt','w',encoding="utf-8")
        str='当前坐标：\n x1:{0}, y1:{1}\n x2:{2}, y2:{3}\n x3:{4}, y3:{5}\n '.format(a[0],a[1],b[0],b[1],c[0],c[1])
        f.write(str)
        f.close()
