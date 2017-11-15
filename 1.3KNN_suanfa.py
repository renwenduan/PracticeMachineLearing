# -*- coding: utf-8 -*-
# Author: DuanRenWen
# Tool: pycharm
# env: python2.7
import KNN
from numpy import *

group,label = KNN.createDataSet()
# KNN 算法
def classfy0(inx, dataSet, label, k):
    dataSetSize = dataSet.shape[0]
    testData = tile(inx,(dataSetSize,1))
    diffMat = testData - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)  #每一行想加
    distances = sqDistances ** 0.5
    sorteDistIndicies = distances.argsort() # 提取索引进行排序,默认从小到大
    classCount = {}
    for i in range(k):
        voteIlabel = label[sorteDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


if __name__ == '__main__':
    classfy0([0,0],group,label,3)