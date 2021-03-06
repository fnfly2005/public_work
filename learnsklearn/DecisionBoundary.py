#!/usr/bin/python
#coding:utf-8
"""
Description: 决策边界可视化
"""
import numpy as np
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import LinearClassifier as lc
plt.switch_backend('agg')

class fitScore(lc.ClassifyPipeline):
    '''模型训练'''
    def __init__(self,X,y,model,param_grid,n_com = 2):
        lc.ClassifyPipeline.__init__(self,train_data=X,train_target=y,\
            linear=model,param_grid=param_grid,n_com=n_com)
        self.X_combined_std = np.vstack((self.X_train,self.X_test))
        self.y_combined = np.hstack((self.y_train,self.y_test))

    def getScorePro(self):
        from sklearn.metrics import accuracy_score
        y_pred = self.linear.predict(self.X_test)
        print (self.y_test != y_pred).sum() #返回错误的样本数
        print '%.2f' % accuracy_score(self.y_test,y_pred) #分类准确率

def plot_decision_regions(X,y,classifier,path_file,test_idx=None,resolution=0.02):#注意无默认参数需置于有默认参数之前
    '''绘出决策边界'''
    markers = ('s','x','o','^','v')#设置标记
    colors = ('red','blue','lightgreen','gray','cyan')#设置颜色
    cmap = ListedColormap(colors[:len(np.unique(y))])
    #两个特征的值域范围
    x1_min, x1_max = X[:,0].min() - 1, X[:,0].max() + 1
    x2_min, x2_max = X[:,1].min() - 1, X[:,1].max() + 1
    #从坐标向量中返回坐标矩阵
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),\
        np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap = cmap) #绘制等高线
    #设置横纵坐标轴范围
    plt.xlim(xx1.min(),xx1.max())
    plt.ylim(xx2.min(),xx2.max())
    #画出所有样本点
    X_test, y_test = X[test_idx, :],y[test_idx]
    for idx,cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl,1],alpha=0.8, c=cmap(idx),\
            marker=markers[idx], label=cl)
    plt.xlabel('petal length [standardized]')
    plt.ylabel('petal width [standardized]')
    plt.legend(loc='upper left') #显示图例
    plt.savefig(path_file)

if __name__ == '__main__':
    from sklearn import datasets
    from sklearn.linear_model import Perceptron
    from sklearn.linear_model import LogisticRegression
    #path = '/Users/fannian/Downloads/'
    path = '/home/fannian/downloads/'
    iris = datasets.load_iris()
    X = iris.data[:,[2,3]]
    y = iris.target

    param_range = [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]
    param_ppn = [{'clf__alpha':param_range}]
    ppn = Perceptron(max_iter=40, eta0=0.001)

    param_log = [{'clf__C':param_range}]
    log = LogisticRegression()

    f = fitScore(X=X,y=y,model=log,param_grid=param_log)
    f.getScoreRro()

    plot_decision_regions(X=f.X_combined_std,y=f.y_combined,classifier=f.linear,\
        test_idx=range(105,150),path_file = path + 'decision_figure.png')
