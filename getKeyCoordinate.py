# -*- coding: UTF-8 -*-
'''
@Description: 获得键盘字母对应的坐标
@Author: LiangCong
@Date: 2018-12-26 15:31:17
@LastEditors: LiangCong
@LastEditTime: 2018-12-30 22:12:53
'''
def getKeyCoordinate():
    letters_1 = "qwertyuiop"
    letters_2 = "asdfghjkl"
    letters_3 = "zxcvbnm"
    letters_1_list = list(letters_1)
    letters_2_list = list(letters_2)
    letters_3_list = list(letters_3)
    key_coordinate_dict = dict()
    # w 键宽
    w = 1.0
    row_pos_1 = 3.0
    column_pos_1 = 0.0
    row_pos_2 = 2.0
    column_pos_2 = 0.3
    row_pos_3 = 1.0
    column_pos_3 = 0.9
    for letter in letters_1_list:
        key_coordinate_dict[letter] = [column_pos_1, row_pos_1]
        column_pos_1 = column_pos_1 + w
    for letter in letters_2_list:
        key_coordinate_dict[letter] = [column_pos_2, row_pos_2]
        column_pos_2 = column_pos_2 + w
    for letter in letters_3_list:
        key_coordinate_dict[letter] = [column_pos_3, row_pos_3]
        column_pos_3 = column_pos_3 + w
    print(key_coordinate_dict)

if __name__ == "__main__":
    getKeyCoordinate()
        