# -*- coding: UTF-8 -*-
'''
@Description: Main
@Author: LiangCong
@Date: 2018-11-27 16:37:18
@LastEditTime: 2018-11-27 18:07:55
@LastEditors: LiangCong
'''

from getMyDistance import getMyDistance

# sample = [[1.0, 2.0], [3.5, 1.0], [2.3, 8.9], [3.6, 8.5], [4.5, 6.7], [1.2, 3.4]]
sample = [[3.5, 6.7], [7.8, 9.0], [1.0, 3.5]]
keyboard = [[3.6, 6.7], [7.8, 9.0], [1.0, 3.5]]
print(getMyDistance(sample, keyboard, 5))