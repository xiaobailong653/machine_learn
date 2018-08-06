#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import preprocessing
import numpy as np


onehot_encoder = DictVectorizer()
instances = [{'city': '北京'}, {'city': '天津'}, {'city': '上海'}]
feature = onehot_encoder.fit_transform(instances).toarray()
print feature


corpus = [
    'UNC played Duke in basketball',
    'Duke lost the basketball game'
]

vectorizer = CountVectorizer()
print vectorizer.fit_transform(corpus).todense()
print vectorizer.vocabulary_

corpus = [
    'The dog ate a sandwich and I ate a sandwich',
    'The wizard transfigured a sandwich'
]

vectorizer = TfidfVectorizer(stop_words='english')
print(vectorizer.fit_transform(corpus).todense())
print(vectorizer.vocabulary_)


X = np.array([
    [0., 0., 5., 13., 9., 1.],
    [0., 0., 13., 15., 10., 15.],
    [0., 3., 15., 2., 0., 11.],
    ])

print preprocessing.scale(X)
