import pandas as pd
from k_means import contour_coefficient
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
import numpy as np

if __name__=="__main__":
    data= pd.read_csv("http://labfile.oss.aliyuncs.com/courses/764/three_class_data.csv",header=0)
    data.head()
    #contuor=contour_coefficient.Contour_coefficient
    #plt=contuor.contour_coefficient(data)
    #plt.show()
    x=data[["x","y"]]
    model = KMeans(n_clusters=3)
    model.fit(x)
    plt.scatter(data['x'],data['y'],c=model.labels_)

    #计算聚类过程的决策边界
    x_min,x_max=data["x"].min()-0.1,data["x"].max()+0.1
    y_min,y_max=data["y"].min()-0.1,data["y"].max()+0.1
    xx,yy=np.meshgrid(np.arange(x_min,x_max,.01),(np.arange(y_min,y_max,.01)))

    result = model.predict(np.c_[xx.ravel(),yy.ravel()])

    #绘制决策边界
    result = result.reshape(xx.shape)
    plt.contourf(xx,yy,result,cmap=plt.cm.Greens)
    plt.scatter(data["x"],data["y"],c=model.labels_,s=15)
    #绘制聚类中心点
    center =model.cluster_centers_
    plt.scatter(center[:,0],center[:,1],marker='p',linewidths=2,color='b',edgecolors='w',zorder=20)
    plt.show()

