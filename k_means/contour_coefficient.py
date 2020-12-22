from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from matplotlib import pyplot as plt

class Contour_coefficient:
    #计算轮廓系数
    @classmethod
    def contour_coefficient(self,data):
        x=data[["x","y"]]
        score=[] #模型建立
        #计算 2 到 12 类的轮廓系数
        for i in range(10):
            model = KMeans(n_clusters=i+2)
            model.fit(x)
            score.append(silhouette_score(x,model.labels_))

        plt.figure(figsize=(11,5))
        plt.subplot(1,2,1)
        plt.scatter(data['x'],data['y'])
        plt.subplot(1,2,2)
        plt.plot(range(2,12,1),score)
        return plt
