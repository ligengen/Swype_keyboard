# -*- coding: UTF-8 -*-
'''
@Description: 根据template单词的首尾字母，以及用户sample滑动的首尾坐标，对可能的单词集合进行初步筛选。
@Author: LiangCong
@Date: 2018-12-18 11:39:13
@LastEditors: LiangCong
@LastEditTime: 2018-12-29 14:24:53
'''

import copy

def templatePruning(begin_sample_position, end_sample_position, all_words, keyboard_position_dict, threshold):
        "⚠️请务必输入float，以及threshold是距离的平方的界值⚠️函数-输入样本点的开始、结束坐标(float)，所有可能的单词集，单词对应坐标的字典，以及距离平方的界值，返回缩小后的单词集合"
        pruned_words = []
        # 遍历所有words
        for word in all_words:
                # 第一步：获取首尾字母
                begin_character = word[0]
                end_character = word[len(word) - 1]
                # 第二步：获取对应的键盘坐标
                begin_character_position = keyboard_position_dict[begin_character]
                end_character_position = keyboard_position_dict[end_character]
                # 第三步：获取首首、尾尾距离之和
                sum = 0
                sum += pow(begin_character_position[0]-begin_sample_position[0], 2) + pow(begin_character_position[1]-begin_sample_position[1], 2)
                sum += pow(end_character_position[0]-end_sample_position[0], 2) + pow(end_character_position[1]-end_sample_position[1], 2)
                # 第四步：判断和threshold的相对大小
                if sum <= threshold:
                    # 可能
                    pruned_words.append(word)
        return pruned_words