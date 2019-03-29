# -*- coding: UTF-8 -*-
'''
@Description: 样本点平移到原点
@Author: LiangCong
@Date: 2018-11-27 16:23:45
@LastEditTime: 2018-12-29 13:24:58
@LastEditors: LiangCong
'''

def sampleTranslation(points):
    "⚠️序列值是非负数，返回值是[list, float, float]⚠️函数-将采集的样本点平移到原点，并返回之后的结果，以及点集中的最大x、y坐标"
    # 遍历获取点的最小x、y，以及最大x、y
    x_min = points[0][0]
    y_min = points[0][1]
    x_max = points[0][0]
    y_max = points[0][1]
    for point in points:
        if point[0] < x_min:
            x_min = point[0]
        if point[0] > x_max:
            x_max = point[0]
        if point[1] < y_min:
            y_min = point[1]
        if point[1] > y_max:
            y_max = point[1]
    # 更新各个点
    new_points = []
    for point in points:
        new_points.append([point[0] - x_min, point[1] - y_min])
    return [new_points, x_max, y_max]