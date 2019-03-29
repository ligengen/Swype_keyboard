# -*- coding: UTF-8 -*-
'''
@Description: 从FittsTime文件中读取单词和对应的Fitts时间
@Author: LiangCong
@Date: 2018-12-19 10:04:07
@LastEditors: LiangCong
@LastEditTime: 2018-12-30 16:58:37
'''
def readFittsTime(dir):
    wordsTimeDict = dict()
    with open(dir, 'r') as f:
        for line in f.readlines():
            wordsTimeDict[line.split(' ')[0]] = float(line.split(' ')[1])
    return wordsTimeDict