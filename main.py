from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from integration import integrate, calc_pruned_lis
from getDistanceDict import getDistanceDict
from calc_x_L import calc_word_dist_lis
from mockSample import mockSample
from readWords.readWords import readWords
from readWords.readFittsTime import readFittsTime
import copy
import datetime


def get_ans(keyboard_position_dict, sample, threshold, L, sigma, r, all_words, fitts_time_dict, t, gamma):
    [shape_dist_dict, template_points_dict] = getDistanceDict(keyboard_position_dict, sample, threshold, L, all_words)

    new_shape_dist_dict = copy.deepcopy(shape_dist_dict)
    new_shape_dist_dict = sorted(new_shape_dist_dict.items(), key=lambda e:e[1], reverse=False)

    print(new_shape_dist_dict)
    # print(template_points_dict)
    # print(sample)
    # for item in sample:
    #     print(item)

    remain_shape_lis = []
    remain_shape_dist = []
    for i in shape_dist_dict:
        remain_shape_lis.append(i)
        remain_shape_dist.append(shape_dist_dict[i])

    word_lis = shape_dist_dict.keys()
    word_dist_lis = calc_word_dist_lis(word_lis, len(sample), template_points_dict, sample, r)

    remain_loc_lis, remain_loc_dist = calc_pruned_lis(sigma, word_lis, word_dist_lis, fitts_time_dict, t, gamma)

    ans_lis = integrate(remain_shape_lis, remain_shape_dist, remain_loc_lis, remain_loc_dist, sigma, fitts_time_dict, t, gamma)
    print(ans_lis)
    return ans_lis


if __name__ == "__main__":
    all_words = readWords('./lexicon_30000.txt')
    fitts_time_dict = readFittsTime('./FittsTime_30000.txt')
    key_coordinate_dict = {'a': [-6.39, 0.32000000000000006], 'c': [-2.38, -1.26], 'b': [0.7800000000000002, -1.26], 'e': [-3.59, 1.9], 'd': [-3.2299999999999995, 0.32000000000000006], 'g': [-0.0699999999999994, 0.32000000000000006], 'f': [-1.6499999999999995, 0.32000000000000006], 'i': [4.3100000000000005, 1.9], 'h': [1.5100000000000007, 0.32000000000000006], 'k': [4.670000000000001, 0.32000000000000006], 'j': [3.0900000000000007, 0.32000000000000006], 'm': [3.9400000000000004, -1.26], 'l': [6.250000000000001, 0.32000000000000006], 'o': [5.890000000000001, 1.9], 'n': [2.3600000000000003, -1.26], 'q': [-6.75, 1.9], 'p': [7.470000000000001, 1.9], 's': [-4.81, 0.32000000000000006], 'r': [-2.01, 1.9], 'u': [2.7300000000000004, 1.9], 't': [-0.4299999999999997, 1.9], 'w': [-5.17, 1.9], 'v': [-0.7999999999999998, -1.26], 'y': [1.1500000000000004, 1.9], 'x': [-3.96, -1.26], 'z': [-5.54, -1.26]}
    sample = mockSample(key_coordinate_dict)
    """sample = [[1.4081212282180786, 0.4787832498550415], [1.4241923093795776, 0.5519716739654541],
              [1.2585713863372803, 0.48106750845909119], [0.64009624719619751, 0.51987957954406738],
              [-0.24864640831947327, 0.94090664386749268], [-1.4035259485244751, 1.3582766056060791],
              [-2.3683440685272217, 1.6645870208740234], [-3.2098653316497803, 1.9894486665725708],
              [-3.4798438549041748, 2.1584291458129883], [-3.0957546234130859, 2.0925662517547607],
              [-1.5762653350830078, 1.7573853731155396], [0.011397019028663635, 1.4839988946914673],
              [1.6892011165618896, 1.0853170156478882], [3.1629271507263184, 0.73086369037628174],
              [4.3665432929992676, 0.36431288719177246], [5.4609780311584473, 0.07635953277349472],
              [5.8973121643066406, -0.027788562700152397], [5.7583065032958984, 0.41438251733779907],
              [5.6780109405517578, 1.4601950645446777], [5.6638789176940918, 2.0076427459716797],
              [5.5765113830566406, 2.1039385795593262]]"""
    t = 10
    gamma = 2.0
    st = datetime.datetime.now()
    get_ans(key_coordinate_dict, sample, 1.5, 15, 0.8, 0.8, all_words, fitts_time_dict, t, gamma)
    ed = datetime.datetime.now()
    print((ed - st).microseconds)

