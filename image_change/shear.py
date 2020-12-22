from tkinter import *
import matplotlib.pyplot as plt
import math

class Shear:
    @classmethod
    def show(self,a,b,c):
        view = Tk()
        view.title('错切变换')
        width,height=(300,100)
        view.geometry("{}x{}".format(width, height))#窗体大小
        fm_top=Frame(view)
        label_top=Label(fm_top,text='错切因子')
        label_top.pack(side=TOP)
        fm_top.pack(side=TOP)
        fm_factor=Frame(view)
        fmx=Frame(fm_factor)
        label_x=Label(fmx,text='水平方向错切因子:')
        label_x.pack(side=LEFT)
        text_x=Entry(fmx)
        text_x.pack(side=RIGHT)
        fmx.pack(side=TOP)
        fmy=Frame(fm_factor)
        label_y=Label(fmy,text='垂直方向错切因子:')
        label_y.pack(side=LEFT)
        text_y=Entry(fmy)
        text_y.pack(side=RIGHT)
        fmy.pack(side=TOP)
        fm_factor.pack(side=LEFT)
        fm_button=Frame(view)
        submit1=Button(fm_button,text='确认',command=lambda:self.shear(self,a,b,c,float(text_x.get()),0))
        submit1.pack(side=TOP)
        submit2=Button(fm_button,text='确认',command=lambda:self.shear(self,a,b,c,float(text_y.get()),1))
        submit2.pack(side=TOP)
        fm_button.pack(side=RIGHT)
        view.mainloop()

    def shear(self,a,b,c,factor,tag):
        factor=math.tan(factor/180.0*math.pi)
        if tag==0:
            x1,y1=a[0]+factor*a[1],a[1]
            x2,y2=b[0]+factor*b[1],b[1]
            x3,y3=c[0]+factor*c[1],c[1]
        else:
            x1,y1=a[0],a[1]+factor*a[0]
            x2,y2=b[0],b[1]+factor*b[0]
            x3,y3=c[0],c[1]+factor*c[0]
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
        plt.title('Shear transformation')
        plt.show()
        f=open('./shear.txt','w',encoding="utf-8")
        str='错切变换后坐标：\n x1:{0}, y1:{1}\n x2:{2}, y2:{3}\n x3:{4}, y3:{5}\n '.format(x1,y1,x2,y2,x3,y3)
        f.write(str)
        f.close()

