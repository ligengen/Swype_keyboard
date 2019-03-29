# -*- coding: UTF-8 -*-
'''
@Description: 获取单词-距离字典
@Author: LiangCong
@Date: 2018-12-19 10:50:35
@LastEditors: LiangCong
@LastEditTime: 2018-12-29 14:26:32
'''
from shapeChannel.getMyDistance import getMyDistance
from templatePruning.templatePruning import templatePruning
import copy

def getDistanceDict(keyboard_position_dict, sample, threshold, L, all_words):
    "threshold为缩减单词组时的界值[距离平方的和](float)，L为shapeChannel归一化时的共长(float)"
    # all_words = ["hello"]
    # 缩减单词集
    # print("缩减单词集合")
    begin_sample_position = sample[0]
    end_sample_position = sample[len(sample)-1]
    possible_words = templatePruning(begin_sample_position, end_sample_position, all_words, 
                    keyboard_position_dict, threshold)
    # print("缩减单词集合完成")
    # 最后获取距离
    words_possibility_dict = dict()
    original_template_points_dict = dict()
    for word in possible_words:
        # 获取单词对应在键盘上的坐标
        keyboard = []
        word_list = list(word)
        for letter in word_list:
            keyboard.append(copy.deepcopy(keyboard_position_dict[letter]))
        # 获取距离
        # print("获取距离"+word)
        [words_possibility_dict[word], original_template_points_dict[word]] = getMyDistance(sample, keyboard, L)
    # 输出结果
    return [words_possibility_dict, original_template_points_dict]
