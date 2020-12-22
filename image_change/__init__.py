from tkinter import *
from image_change import show
from image_change import translate
from image_change import rotation
from image_change import scaling
from image_change import shear
from image_change import reflection

class my_gui(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.window_init()
        self.creatFrame()
        self.pack()


    def window_init(self):
        self.master.title('图形几何变换')
        width,height=(500,200)
        self.master.geometry("{}x{}".format(width, height))#窗体大小


    def creatFrame(self):
        #fm1标题
        self.fm1=Frame(self)
        self.titleLabel=Label(self.fm1,text='点的坐标')
        self.titleLabel.pack()
        self.fm1.pack()
        #fm2输入点坐标
        self.fm2=Frame(self)
        #左侧放X坐标
        self.fm2_left=Frame(self.fm2)

        self.fm2_left_X1=Frame(self.fm2_left)
        self.label_x1=Label(self.fm2_left_X1,text='X1: ')
        self.label_x1.pack(side=LEFT)
        self.text_x1=Entry(self.fm2_left_X1,textvariable=StringVar(value=12))
        self.text_x1.pack(side=RIGHT)
        self.fm2_left_X1.pack(side=TOP)

        self.fm2_left_X2=Frame(self.fm2_left)
        self.label_x2=Label(self.fm2_left_X2,text='X2: ')
        self.label_x2.pack(side=LEFT)
        self.text_x2=Entry(self.fm2_left_X2,textvariable=StringVar(value=7))
        self.text_x2.pack(side=RIGHT)
        self.fm2_left_X2.pack(side=TOP)

        self.fm2_left_X3=Frame(self.fm2_left)
        self.label_x3=Label(self.fm2_left_X3,text='X3: ')
        self.label_x3.pack(side=LEFT)
        self.text_x3=Entry(self.fm2_left_X3,textvariable=StringVar(value=21))
        self.text_x3.pack(side=RIGHT)
        self.fm2_left_X3.pack(side=TOP)

        #右侧放Y坐标
        self.fm2_right=Frame(self.fm2)

        self.fm2_right_Y1=Frame(self.fm2_right)
        self.label_y1=Label(self.fm2_right_Y1,text='Y1: ')
        self.label_y1.pack(side=LEFT)
        self.text_y1=Entry(self.fm2_right_Y1,textvariable=StringVar(value=35))
        self.text_y1.pack(side=RIGHT)
        self.fm2_right_Y1.pack(side=TOP)

        self.fm2_right_Y2=Frame(self.fm2_right)
        self.label_y2=Label(self.fm2_right_Y2,text='Y2: ')
        self.label_y2.pack(side=LEFT)
        self.text_y2=Entry(self.fm2_right_Y2,textvariable=StringVar(value=24))
        self.text_y2.pack(side=RIGHT)
        self.fm2_right_Y2.pack(side=TOP)

        self.fm2_right_Y3=Frame(self.fm2_right)
        self.label_y3=Label(self.fm2_right_Y3,text='Y3: ')
        self.label_y3.pack(side=LEFT)
        self.text_y3=Entry(self.fm2_right_Y3,textvariable=StringVar(value=14))
        self.text_y3.pack(side=RIGHT)
        self.fm2_right_Y3.pack(side=TOP)

        self.fm2_left.pack(side=LEFT)
        self.fm2_right.pack(side=RIGHT)
        self.fm2.pack(side=TOP)

        #fm3各个函数按键
        self.fm3=Frame(self)
        self.fm3_left=Frame(self.fm3)

        self.fm3_left_button1=Frame(self.fm3_left)
        func1=show.Show
        self.fm3_button1=Button(self.fm3_left_button1,text='绘制图形',command=lambda:func1.show([float(self.text_x1.get()),float(self.text_y1.get())],[float(self.text_x2.get()),float(self.text_y2.get())],[float(self.text_x3.get()),float(self.text_y3.get())]))
        self.fm3_button1.pack(side=LEFT)
        func2=translate.Translate
        self.fm3_button2=Button(self.fm3_left_button1,text='平移变换',command=lambda:func2.show([float(self.text_x1.get()),float(self.text_y1.get())],[float(self.text_x2.get()),float(self.text_y2.get())],[float(self.text_x3.get()),float(self.text_y3.get())]))
        self.fm3_button2.pack(side=RIGHT)
        self.fm3_left_button1.pack(side=TOP)

        self.fm3_left_button2=Frame(self.fm3_left)
        func4=scaling.Scaling
        self.fm3_button3=Button(self.fm3_left_button2,text='缩放变换',command=lambda:func4.show([float(self.text_x1.get()),float(self.text_y1.get())],[float(self.text_x2.get()),float(self.text_y2.get())],[float(self.text_x3.get()),float(self.text_y3.get())]))
        self.fm3_button3.pack(side=LEFT)
        func5=shear.Shear
        self.fm3_button4=Button(self.fm3_left_button2,text='错切变换',command=lambda:func5.show([float(self.text_x1.get()),float(self.text_y1.get())],[float(self.text_x2.get()),float(self.text_y2.get())],[float(self.text_x3.get()),float(self.text_y3.get())]))
        self.fm3_button4.pack(side=RIGHT)
        self.fm3_left_button2.pack(side=TOP)

        self.fm3_right=Frame(self.fm3)

        self.fm3_right_button1=Frame(self.fm3_right)
        func3=rotation.Rotation
        self.fm3_button5=Button(self.fm3_right_button1,text='旋转变换',command=lambda:func3.show([float(self.text_x1.get()),float(self.text_y1.get())],[float(self.text_x2.get()),float(self.text_y2.get())],[float(self.text_x3.get()),float(self.text_y3.get())]))
        self.fm3_button5.pack()
        self.fm3_right_button1.pack(side=TOP)

        self.fm3_right_button2=Frame(self.fm3_right)
        func6=reflection.Reflection
        self.fm3_button6=Button(self.fm3_right_button2,text='反射变换',command=lambda:func6.show([float(self.text_x1.get()),float(self.text_y1.get())],[float(self.text_x2.get()),float(self.text_y2.get())],[float(self.text_x3.get()),float(self.text_y3.get())]))
        self.fm3_button6.pack()
        self.fm3_right_button2.pack(side=TOP)



        self.fm3_left.pack(side=LEFT)
        self.fm3_right.pack(side=RIGHT)
        self.fm3.pack(side=TOP)

if __name__ == '__main__':
    init_window=my_gui()
    init_window.mainloop()

