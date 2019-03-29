# -*- coding: UTF-8 -*-
'''
@Description: 从文件中读取所有可能的单词序列
@Author: LiangCong
@Date: 2018-12-19 10:04:07
@LastEditors: LiangCong
@LastEditTime: 2018-12-19 10:20:16
'''
def readWords(dir):
    words = []
    with open(dir, 'r') as f:
        for line in f.readlines():
            words.append(line.split(' ')[0])
    return words