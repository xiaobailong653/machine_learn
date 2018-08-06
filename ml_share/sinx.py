#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

plt.figure()
plt.title("sin(x) and cos(x)")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.axis([-12, 12, -1, 1])
plt.grid(True)
xx = np.linspace(-12, 12, 1000)
plt.plot(xx, np.sin(xx), 'g-', label="$sin(x)$")
plt.plot(xx, np.cos(xx), 'r--', label="$cos(x)$")
plt.legend()
plt.show()
