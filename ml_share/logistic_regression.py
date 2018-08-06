#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model.logistic import LogisticRegression

X = []

X.append("fuck you")
X.append("fuck you all")
X.append("hello everyone")

X.append("fuck me")
X.append("hello boy")

y = [1, 1, 0]

vectorizer = TfidfVectorizer()

# 取X的前三句作为输入做tfidf转换
X_train = vectorizer.fit_transform(X[:-2])

# 取X的后两句用上面生成的tfidf做转换
X_test = vectorizer.transform(X[-2:])

# 用逻辑回归模型做训练
classifier = LogisticRegression()
classifier.fit(X_train, y)

# 做测试样例的预测
predictions = classifier.predict(X_test)
print predictions
