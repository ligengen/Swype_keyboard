# -*- coding: UTF-8 -*-
'''
@Description: 输入两个序列，获得距离
@Author: LiangCong
@Date: 2018-11-27 18:23:13
@LastEditors: LiangCong
@LastEditTime: 2018-12-29 13:42:00
'''

from sampleTranslation import sampleTranslation
from keyboardTranslation import keyboardTranslation
from shapeNormalizedDistance import shapeNormalizedDistance

def getMyDistance(sample_points, keyboard_points, L):
    "函数-输入样本、键盘序列与归一化时的共长L，返回距离值"
    [new_sample_points, sample_x_max, sample_y_max] = sampleTranslation(sample_points)
    [new_keyboard_points, keyboard_x_max, keyboard_y_max, original_template_points] = keyboardTranslation(keyboard_points, len(sample_points))
    
    distance = shapeNormalizedDistance(new_sample_points, sample_x_max, sample_y_max, new_keyboard_points, keyboard_x_max, keyboard_y_max, L)
    return [distance, original_template_points]