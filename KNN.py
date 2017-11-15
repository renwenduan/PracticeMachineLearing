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

def file2matrix(filename):
    fr = open(filename)
    arrayOlines = fr.readlines()
    numberOflines = len(arrayOlines)
    returnMat = zeros((numberOflines,3))
    classLabelVector = []
    index = 0
    for line in arrayOlines:
        line = line.strip()
        listFromLine = line.split('\t')[0].split(',')
        returnMat[index,:] = listFromLine[0:3]  # 第一行赋值
        classLabelVector.append(int(listFromLine[-1])) # 把第四行的数据单一提取出来
        index += 1
    return returnMat, classLabelVector


def autoNorm(dataset):
    max_vals = dataset.max(0)
    minvals = dataset.min(0)
    ranges = dataset - minvals
    norm_data_set = zeros(shape(dataset))
    m = dataset.shape[0]
    norm_data_set = dataset - tile(minvals, (m, 1))
    norm_data_set = norm_data_set / tile(ranges, (m, 1))
    return norm_data_set, ranges, minvals

datingDataMat,datingLabels = file2matrix(r'dating_data.csv')