# -*- coding: UTF-8 -*-
'''
@Description: 距离计算
@Author: LiangCong
@Date: 2018-11-27 17:58:55
@LastEditors: LiangCong
@LastEditTime: 2018-12-29 13:34:26
'''


def shapeNormalizedDistance(points_sample, sample_x_max, sample_y_max, points_template, template_x_max, template_y_max, L):
    "⚠️请务必输入float，务必保证两个序列已经平移到0，且长度相等，且序列值是非负数⚠️函数-输入模版点和键盘点与归一化时的共长L，返回二者的距离"
    # 先检查二者的长度是否一致
    # if len(points_sample) != len(points_sample):
    #     return
    # 然后进行尺度放缩，策略是，让两块图像矩形外框的最长边相等
    # 第一步，得到最长的边
    longest_edge_sample = 0
    longest_edge_template = 0
    if sample_x_max > sample_y_max:
        longest_edge_sample = sample_x_max
    else:
        longest_edge_sample = sample_y_max
    if template_x_max > template_y_max:
        longest_edge_template = template_x_max
    else:
        longest_edge_template = template_y_max
    # 第二步，得到比例，将最长的边设置为等长L
    L = float(L)
    L_sample_ratio = L / longest_edge_sample
    L_template_ratio = L / longest_edge_template
    # 第三步， 变换点
    new_points_sample = []
    new_points_template = []
    for point in points_sample:
        new_points_sample.append([point[0]*L_sample_ratio, point[1]*L_sample_ratio])
    for point in points_template:
        new_points_template.append([point[0]*L_template_ratio, point[1]*L_template_ratio])
    # 第四步，计算距离
    sum = 0
    length = 0
    length_sample = len(new_points_sample)
    length_keyboard = len(new_points_template)
    if length_sample > length_keyboard:
        length = length_keyboard
    else:
        length = length_sample
    for i in range(0,length):
        sum += ((new_points_sample[i][0]-new_points_template[i][0]) ** 2 + (new_points_sample[i][1]-new_points_template[i][1]) ** 2) ** 0.5
    # 第五步，计算平均距离
    sum = sum / len(new_points_sample)
    return sum