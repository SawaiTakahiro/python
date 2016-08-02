#http://qiita.com/puriketu99/items/c519a95c0b16ea63c1ac より
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 10)

y = x**2

plt.plot(x, y)
plt.show()