# coding=utf-8
'''
-------------------------------------------------
Author: RenWen
Product Name: PyCharm
Date:  17/11/14
-------------------------------------------------
'''
from numpy import *


def autoNorm(dataset):
    max_vals = dataset.max(0)
    minvals = dataset.min(0)
    ranges = dataset - minvals
    norm_data_set = zeros(shape(dataset))
    m = dataset.shape[0]
    norm_data_set = dataset - tile(minvals, (m, 1))
    norm_data_set = norm_data_set / tile(ranges, (m, 1))
    return norm_data_set, ranges, minvals


def dating_data_mat:
    '''
    这里应该是使用之前的数据,这里未导入等待导入
    :return:
    '''
    pass


if __name__ == '__main__':
    norm_mat, ranges, min_vals = autoNorm(dating_data_mat)
    print norm_mat
