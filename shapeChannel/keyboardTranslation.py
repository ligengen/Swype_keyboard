# -*- coding: UTF-8 -*-
'''
@Description: 生成键盘template点并平移到原点
@Author: LiangCong
@Date: 2018-11-27 16:46:27
@LastEditors: LiangCong
@LastEditTime: 2018-12-30 22:36:15
'''


from sampleTranslation import sampleTranslation
import math
import copy

def keyboardTranslation(keyboard_points, N):
    "⚠️请务必输入float，且序列值是非负数⚠️函数-输入对应template在键盘上的点（有几个按键就有几个点），以及样本的点个数(用来规划分点)，返回对键盘处理后的键盘点，其中这些点已经平移到原点了"
    distance = []
    points = []
    length = len(keyboard_points)
    # 如果不止一个点
    if length > 1:
        # 第一步，计算各个点之间的距离
        for i in range(0,(length-1)):
            d = ((keyboard_points[i][0] - keyboard_points[i+1][0]) ** 2 + (keyboard_points[i][1] - keyboard_points[i+1][1]) ** 2) ** 0.5
            distance.append(d)
        # 第二步，求距离比例
        distance_ratio = []
        # 如果分母为0，则直接按1/n计算比例
        if sum(distance) == 0:
            for i in range(0, (length - 1)):
                distance_ratio.append(1 / len(distance))
        else:
            for i in range(0,(length-1)):
                distance_ratio.append(distance[i] / sum(distance))
        # print(distance_ratio)
        # 第三步，求具体每段的点数
        point_num = []
        for i in range(0, (length-2)):
            # print("--------------------------------------")
            # print(i)
            # print(distance_ratio[i])
            # print(distance[0])
            # print(sum(distance))
            point_num.append(int(math.floor(N * distance_ratio[i])))
        point_num.append(N-sum(point_num))
        # 第四步，对每一段具体求点
        for i in range(0, (length-1)):
            if point_num[i] == 1 or point_num[i] == 0:
                if point_num[i] == 1:
                    # 对于只有一个点的情况，直接返回该段中间的点
                    points.append([(keyboard_points[i][0]+keyboard_points[i+1][0])/2,
                    (keyboard_points[i][1]+keyboard_points[i+1][1])/2])
            else:
                a = (keyboard_points[i+1][0]-keyboard_points[i][0]) / (point_num[i]-1)
                b = (keyboard_points[i+1][1]-keyboard_points[i][1]) / (point_num[i]-1)
                for j in range(0,(point_num[i])):
                    point_x = (keyboard_points[i][0]) + a*j
                    poiny_y = (keyboard_points[i][1]) + b*j
                    points.append([point_x, poiny_y])
    else:
        points = [keyboard_points[0]]
    
    while len(points) < N:
        points.append(keyboard_points[len(keyboard_points)-1])

    # 第五步，对得到的点 Normalize 到原点
    [translated_points, x_max, y_max] = sampleTranslation(copy.deepcopy(points))

    return [translated_points, x_max, y_max, points]
        
