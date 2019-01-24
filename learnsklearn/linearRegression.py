#!/usr/bin/python
# coding: utf-8
from sklearn import datasets #数据集模块
from sklearn import preprocessing #特征处理模块
from sklearn import linear_model #广义线性模块
from sklearn import model_selection #模型选择模块
import pandas as pd
import matplotlib.pyplot as plt

#支持外部导入数据，返回的数列可直接应用train_test_split函数
def loadData(datefile):
    df = pd.read_csv(datefile,sep='\t')# 读取数据
    df['日期']=pd.to_datetime(df['日期'],format='%Y-%m-%d')
    return df[["日期","订单量"]].sort_values(by='日期')

#输入特征和特征标签，输出线性分类器评估值
def linearMethod(train_data,train_target):
    X_train,X_test, y_train, y_test = model_selection.train_test_split(train_data,train_target,test_size=0.2)#切分数据集

    #linear=linear_model.LinearRegression(normalize=True)#最小二乘法，设置normalize参数对特征进行缩放
    linear=linear_model.Ridge(alpha= 0.1,normalize=True)#岭回归，设置normalize参数对特征进行缩放，设置alpha惩罚系数-默认0.5

    linear.fit(X_train,y_train)#训练模型参数

    print "linear's score: ",linear.score(X_train,y_train)#评分函数，返回R方，拟合优度
    print "predict: ",linear.predict(X_test)#分类器应用
    print y_test

if __name__ == '__main__':
    boston = datasets.load_boston()#导入数据集,波士顿房价数据
    linearMethod(boston.data,boston.target)#获取特征向量,获得样本标签,应用至模型
