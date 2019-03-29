# -*- coding: UTF-8 -*-
'''
@Description: 按照Fitts' Law获取输入单词的标准时间
@Author: LiangCong
@Date: 2018-12-26 16:32:01
@LastEditors: LiangCong
@LastEditTime: 2018-12-29 16:09:24
'''
import math

def getFittsTime(word, key_coordinate_dict, W):
    "输入为单词、键盘字母坐标、键宽⚠️获取根据Fitts's Law计算的单词word的输入时间(ms)"
    a = 83
    b = 127
    N = len(word)
    sum_of_log = 0
    for i in range(0, N-1):
        point_1 = key_coordinate_dict[word[i]]
        point_2 = key_coordinate_dict[word[i+1]]
        distance = ((point_1[0]-point_2[0]) ** 2 + (point_1[1]-point_2[1]) ** 2) ** 0.5
        sum_of_log += math.log(distance / W + 1, 2)
    t = N * a + b * sum_of_log
    return t