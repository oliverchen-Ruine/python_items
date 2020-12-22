import matplotlib.pylab as plt
import numpy as np
data = np.load(r"C:\Users\olive\Desktop\study\python\国民经济核算季度数据.npz",allow_pickle=True)
name=data["columns"]#列标题
values = data["values"]#值
plt.rcParams["font.sans-serif"] = "SimHei"    #中文字体正常显示
plt.rcParams["axes.unicode_minus"] = False   #特殊符号正常显示

#绘制画布
plt.figure(figsize=(10,10),dpi=500)
plt.title("国民经济核算图表")
#X,Y轴标题
plt.xlabel("年份")
plt.ylabel("生产总值（亿元）")
plt.xlim()
plt.ylim((0,np.max(values[:,2])+20000))
plt.xticks(range(0,70,4),values[range(0,70,4),1],rotation = 45)
plt.yticks(np.arange(0,230000,10000))
plt.plot(values[:,2],marker="o",c="yellow")
plt.plot(values[:,3],marker="D",c="blue")
plt.plot(values[:,4],marker="*",c="red")
plt.plot(values[:,5],marker="+",c="green")

# 保存并显示
plt.savefig(r"C:\Users\olive\Desktop\study\python\国民经济核算图表.pdf")
plt.show()