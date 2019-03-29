# -*- coding: UTF-8 -*-
'''
@Description: 生成单词的Fitts Time文件
@Author: LiangCong
@Date: 2018-12-29 15:53:42
@LastEditors: LiangCong
@LastEditTime: 2018-12-30 20:08:19
'''
from getFittsTime import getFittsTime

def generateFittsTimeFile(read_dir, key_coordinate_dicts, W, write_dir):
    words = []
    with open(read_dir, 'r') as f:
        for line in f.readlines():
            words.append(line.split(' ')[0])
    with open(write_dir, 'w') as f:
        for word in words:
            f.write(word + ' ' + str(getFittsTime(word, key_coordinate_dicts, W)) + '\n')
