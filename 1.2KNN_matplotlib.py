# -*- coding: utf-8 -*-
# Author: DuanRenWen
# Tool: pycharm
# env: python
from KNN_example import datingDataMat,datingLabels
import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
plt.show()
