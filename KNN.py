# -*- coding: utf-8 -*-
# Author: DuanRenWen
# Tool: pycharm
# env: python
from numpy import *
import operator  # 这是运算符模块

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

