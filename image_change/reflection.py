from tkinter import *
import matplotlib.pyplot as plt

class Reflection:
    @classmethod
    def show(self,a,b,c):
        view = Tk()
        view.title('反射变换')
        width,height=(200,50)
        view.geometry("{}x{}".format(width, height))#窗体大小
        fm_button=Frame(view)
        fm_button1=Frame(fm_button)
        submit1=Button(fm_button1,text='X轴',command=lambda:self.reflection(self,a,b,c,0))
        submit1.pack(side=LEFT)
        submit2=Button(fm_button1,text='Y轴',command=lambda:self.reflection(self,a,b,c,1))
        submit2.pack(side=RIGHT)
        fm_button2=Frame(fm_button)
        submit3=Button(fm_button2,text='原点',command=lambda:self.reflection(self,a,b,c,2))
        submit3.pack(side=TOP)
        fm_button.pack(side=TOP)
        fm_button1.pack(side=LEFT)
        fm_button2.pack(side=RIGHT)
        view.mainloop()

    def reflection(self,a,b,c,tag):
        flag=''
        if tag==0:
            x1,y1=a[0],-a[1]
            x2,y2=b[0],-b[1]
            x3,y3=c[0],-c[1]
            flag='X轴'
        elif tag==1:
            x1,y1=-a[0],a[1]
            x2,y2=-b[0],b[1]
            x3,y3=-c[0],c[1]
            flag='Y轴'
        else:
            x1,y1=-a[0],-a[1]
            x2,y2=-b[0],-b[1]
            x3,y3=-c[0],-c[1]
            flag='原点'
        fig=plt.figure()
        ax = fig.add_subplot(111)
        pgon1 = plt.Polygon((a,b,c), color ='g', alpha = 0.5 )
        plt.annotate(r'$%s$' % 'before',xy=(a[0],a[1]),xycoords='data',xytext=(+30,-30),
             textcoords='offset points',fontsize=7,
             arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))
        pgon2 = plt.Polygon(([x1,y1],[x2,y2],[x3,y3]), color ='r', alpha = 0.5 )
        plt.annotate(r'$%s$' % 'after',xy=(x1,y1),xycoords='data',xytext=(+30,-30),
             textcoords='offset points',fontsize=7,
             arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))
        ax.add_patch(pgon1)
        ax.add_patch(pgon2)
        plt.plot()
        plt.title('reflection transformation')
        plt.show()
        f=open('./reflection.txt','w',encoding="utf-8")
        str='对{6}变换变换后坐标：\n x1:{0}, y1:{1}\n x2:{2}, y2:{3}\n x3:{4}, y3:{5}\n '.format(x1,y1,x2,y2,x3,y3,flag)
        f.write(str)
        f.close()