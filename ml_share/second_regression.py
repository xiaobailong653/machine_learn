#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

plt.figure()
plt.title("Polynomial regression")
plt.xlabel('x')
plt.ylabel('y')
plt.axis([30, 400, 100, 400])
plt.grid(True)

X =[[50], [100], [150], [200], [250], [300]]
y = [[150], [200], [250], [280], [310], [330]]
X_test = [[250], [300]]
y_test = [[310], [330]]

plt.plot(X, y, 'k.')

model = LinearRegression()
model.fit(X, y)
X2 = [[30], [400]]
y2 = model.predict(X2)
plt.plot(X2, y2, 'g-')

xx = np.linspace(30, 400, 100)
quadratic_featurizer = PolynomialFeatures(degree=2)
X_train_quadratic = quadratic_featurizer.fit_transform(X)
xx_quadratic = quadratic_featurizer.transform(xx.reshape(xx.shape[0], 1))
regressor_quadratic = LinearRegression()
regressor_quadratic.fit(X_train_quadratic, y)
plt.plot(xx, regressor_quadratic.predict(xx_quadratic), 'r-')

cubic_featurizer = PolynomialFeatures(degree=3)
X_train_cubic = cubic_featurizer.fit_transform(X)
regressor_cubic = LinearRegression()
regressor_cubic.fit(X_train_cubic, y)
xx_cubic = cubic_featurizer.transform(xx.reshape(xx.shape[0], 1))
plt.plot(xx, regressor_cubic.predict(xx_cubic))


plt.show()

print '一元回归：r-squared =', model.score(X_test, y_test)
X_test_quadratic = quadratic_featurizer.transform(X_test)
print '二元回归：r-squared =', regressor_quadratic.score(X_test_quadratic, y_test)
X_test_cubic = cubic_featurizer.transform(X_test)
print '三元回归：r-squared =', regressor_cubic.score(X_test_cubic, y_test)
