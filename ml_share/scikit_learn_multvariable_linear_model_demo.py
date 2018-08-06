#!/usr/bin/env python
# -*- coding: utf-8 -*-
from numpy.linalg import inv
from numpy import dot, transpose
from numpy.linalg import lstsq
from sklearn.linear_model import LinearRegression


X = [[1, 1, 1], [1, 1, 2], [1, 2, 1]]
y = [[6], [9], [8]]

'''
transpose: 求转置
dot: 求矩阵乘积
inv: 求矩阵的逆
(XtX)-1XtY=β
'''
beta = dot(inv(dot(transpose(X), X)), dot(transpose(X), y))
print "β = ", beta

beta = lstsq(X, y)[0]
print "β = ", beta

model = LinearRegression()
model.fit(X, y)
p_x = [[1, 3, 5]]
p_y = model.predict(p_x)
print p_y
