#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


x = [[1], [2], [3], [4], [5], [6]]
y = [[1], [2.1], [2.9], [4.2], [5.1], [5.8]]

plt.figure()
plt.xlabel('X axis')
plt.ylabel('Y axis')


def linear_regression():
    '''根据线性回归预测'''
    # 创建线性回归模型
    model = LinearRegression()
    model.fit(x, y)
    # 这个会报错
    # predicted = model.predict([13])[0]

    # 预测13
    p_x = [[13]]
    p_y = model.predict(p_x)
    print p_y

    # 线性回归绘图
    plt.title('Linear Regression')

    # 坐标轴的范围
    plt.axis([0, 25, 0, 25])
    # 显示网格
    plt.grid(True)

    # 现有点的分布
    plt.plot(x, y, 'k.')
    # 预测店的分布
    plt.plot(p_x, p_y, "r+")
    plt.show()


def variance():
    '''根据方差和协方差预测'''
    xx = [item[0] for item in x]
    yy = [item[0] for item in y]

    var = np.var(xx, ddof=1)        # 方差计算
    cov = np.cov(xx, yy)[0][1]      # 协方差计算

    # 计算线性方程的参数b, 方差除以协方差
    b = var / cov
    print "参数：", b
    p_x = 13

    # 计算偏置项a
    a = 1 - b * 1
    print "偏置项：", a
    p_y = b * p_x + a
    print "y = ", p_y

    # 线性回归绘图
    plt.title('variance')

    # 坐标轴的范围
    plt.axis([0, 25, 0, 25])
    # 显示网格
    plt.grid(True)

    # 现有点的分布
    plt.plot(x, y, 'k.')
    # 预测店的分布
    plt.plot([[p_x]], [[p_y]], "r+")
    plt.show()

if __name__ == '__main__':
    variance()
