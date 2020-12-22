from tkinter import *
import math
import matplotlib.pyplot as plt
class Rotation:
    @classmethod
    def show(self,a,b,c):
        view = Tk()
        view.title('旋转变换')
        width,height=(200,100)
        view.geometry("{}x{}".format(width, height))#窗体大小
        fm_top=Frame(view)
        label_top=Label(fm_top,text='旋转角度')
        label_top.pack(side=TOP)
        fm_top.pack(side=TOP)
        fmx=Frame(view)
        label_x=Label(fmx,text='angle:')
        label_x.pack(side=LEFT)
        text_x=Entry(fmx)
        text_x.pack(side=RIGHT)
        fmx.pack(side=TOP)
        fm_button=Frame(view)
        submit=Button(fm_button,text='确认',command=lambda:self.rotation(self,a,b,c,float(text_x.get())))
        submit.pack(side=TOP)
        fm_button.pack(side=TOP)
        view.mainloop()


    def rotation(self,a,b,c,angle):
        angle=angle*math.pi/180.0
        cosA=math.cos(angle)
        sinA=math.sin(angle)
        #以(0.0)为旋转中心点
        x1,y1=a[0]*cosA-a[1]*sinA,a[0]*sinA+a[1]*cosA
        x2,y2=b[0]*cosA-b[1]*sinA,b[0]*sinA+b[1]*cosA
        x3,y3=c[0]*cosA-c[1]*sinA,c[0]*sinA+c[1]*cosA
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
        plt.title('rotation transformation')
        plt.show()
        f=open('./rotation.txt','w',encoding="utf-8")
        str='旋转变换后坐标：\n x1:{0}, y1:{1}\n x2:{2}, y2:{3}\n x3:{4}, y3:{5}\n '.format(x1,y1,x2,y2,x3,y3)
        f.write(str)
        f.close()
