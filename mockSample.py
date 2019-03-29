# -*- coding: UTF-8 -*-
'''
@Description: 获取模拟的用户输入列表
@Author: LiangCong
@Date: 2018-12-26 15:58:06
@LastEditors: LiangCong
@LastEditTime: 2018-12-29 14:07:38
'''
def mockSample(key_coordinate_dict):
    sample = []
    input_string = raw_input("请滑动输入\n")
    # input_string = "trtyuytre"
    input_string_list = list(input_string)
    for letter in input_string_list:
        sample.append(key_coordinate_dict[letter])
    return sample
if __name__ == "__main__":
    mockSample({'a': [2.0, 0.3], 'c': [1.0, 2.9], 'b': [1.0, 4.9], 'e': [3.0, 2.0], 'd': [2.0, 2.3], 'g': [2.0, 4.3], 'f': [2.0, 3.3], 'i': [3.0, 7.0], 'h': [2.0, 5.3], 'k': [2.0, 7.3], 'j': [2.0, 6.3], 'm': [1.0, 6.9], 'l': [2.0, 8.3], 'o': [3.0, 8.0], 'n': [1.0, 5.9], 'q': [3.0, 0.0], 'p': [3.0, 9.0], 's': [2.0, 1.3], 'r': [3.0, 3.0], 'u': [3.0, 6.0], 't': [3.0, 4.0], 'w': [3.0, 1.0], 'v': [1.0, 3.9], 'y': [3.0, 5.0], 'x': [1.0, 1.9], 'z': [1.0, 0.9]})