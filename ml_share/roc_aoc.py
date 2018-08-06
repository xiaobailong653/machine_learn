#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc


false_positive_rate, recall, thresholds = roc_curve(pred, predictions)
roc_auc = auc(false_positive_rate, recall)
plt.plot(false_positive_rate, recall, 'b', label='AUC = %0.2f' % roc_auc)
plt.show()
