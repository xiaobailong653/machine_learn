#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist


def demo(n_clusters):
    # 生成2×10的矩阵，且值均匀分布的随机数
    cluster1 = np.random.uniform(0.5, 1.5, (2, 10))
    cluster2 = np.random.uniform(3.5, 4.5, (2, 10))

    # 顺序连接两个矩阵，形成一个新矩阵，所以产生了2*20的矩阵，T做转置后变成20*2的矩阵
    X = np.hstack((cluster1, cluster2)).T

    plt.figure()
    plt.axis([0, 5, 0, 5])
    plt.grid(True)
    plt.plot(X[:, 0], X[:, 1], 'k.')


    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(X)
    plt.plot(kmeans.cluster_centers_[:,0],
             kmeans.cluster_centers_[:,1], 'ro')
    plt.show()


def zhoubufaze():
    cluster1 = np.random.uniform(0.5, 1.5, (2, 10))
    cluster2 = np.random.uniform(1.5, 2.5, (2, 10))
    cluster3 = np.random.uniform(1.5, 3.5, (2, 10))
    cluster4 = np.random.uniform(3.5, 4.5, (2, 10))

    X1 = np.hstack((cluster1, cluster2))
    X2 = np.hstack((cluster3, cluster4))
    X = np.hstack((X1, X2)).T

    K = range(1, 10)
    meandistortions = []
    for k in K:
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(X)
        # 求kmeans的成本函数值
        meandistortions.append(
            sum(np.min(
                cdist(X,
                      kmeans.cluster_centers_,
                      'euclidean'), axis=1)) / X.shape[0])

    plt.figure()
    plt.grid(True)
    plt1 = plt.subplot(2, 1, 1)
    # 画样本点
    plt1.plot(X[:,0], X[:,1], 'k.')
    plt2 = plt.subplot(2, 1, 2)
    # 画成本函数值曲线
    plt2.plot(K, meandistortions, 'bx-')
    plt.show()


if __name__ == '__main__':
    zhoubufaze()
