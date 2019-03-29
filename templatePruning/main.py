# -*- coding: UTF-8 -*-
'''
@Description: 测试templatePruning
@Author: LiangCong
@Date: 2018-12-18 11:59:20
@LastEditors: LiangCong
@LastEditTime: 2018-12-19 10:35:41
'''

from templatePruning import templatePruning

begin_sample_position = [1.0, 2.0]
end_sample_position = [8.0, 9.0]
all_words = ["hello", "it", "is", "me"]
keyboard_position_dict ={"h":[2.0, 3.0], "o":[8.0, 9.0], "i":[33.0, 12.0], 
                        "t":[55.0, 66.0], "s":[11.0, 22.0], "m":[7.0, 8.0], 
                        "e":[1.0, 2.0]}
threshold = 10000
possible_words = templatePruning(begin_sample_position, end_sample_position, all_words, 
                keyboard_position_dict, threshold)
print(possible_words)
