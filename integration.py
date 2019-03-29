from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
import math


def calc_p_x(sigma, distance):
    """
    input has 'distance' to template y. y fixed

    :param sigma: param, to be fine-tuned. (a key radius could be right)
    :param distance: shape channel and location channel distance
    :return: the prob of the template y
    """
    return 1 / (sigma * ((2 * math.pi) ** 0.5)) * math.exp(- 1 / 2 * ((distance / sigma) ** 2))


def calc_pruned_lis(sigma, word_list, dist_list, fitts_time_dict, t, gamma):
    pruned_lis = []
    pruned_dis_lis = []
    for idx, i in enumerate(word_list):
        new_sigma = sigma
        gamma = 2.0
        if t >= fitts_time_dict[i]:
            new_sigma = sigma
        else:
            new_sigma = sigma * (1 + gamma * math.log(t/fitts_time_dict[i]))
        if calc_p_x(new_sigma, dist_list[idx]) != 0:
            pruned_lis.append(i)
            pruned_dis_lis.append(dist_list[idx])
    return pruned_lis, pruned_dis_lis


'''def calc_word_prob(remaining_word_candidate, remaining_word_dist, sigma, word):
    fu za du tai gao le
    """
    :param remaining_word_candidate: a list of template candidates
    :param remaining_word_dist: a list of calculated distance. Same size as word_candidate
    :param sigma: param, to be fine-tuned. (a key radius could be right)
    :param word:
    :return:
    """
    btm = 0
    for idx, i in enumerate(remaining_word_candidate):
        btm += calc_p_x(sigma, remaining_word_dist[idx])
    if btm == 0:
        raise ValueError("btm is zero!")
    ans_idx = -1
    for idx, i in enumerate(remaining_word_candidate):
        if word == i:
            ans_idx = idx
            break
    if ans_idx == -1:
        raise ValueError("no such word in word_candidate!")
    return calc_p_x(sigma, remaining_word_dist[ans_idx]) / btm'''


def calc_word_prob(remaining_word_candidate, remaining_word_dist, sigma, fitts_time_dict, t, gamma):
    """
    :param remaining_word_candidate: a list of template candidates
    :param remaining_word_dist: a list of calculated distance. Same size as word_candidate
    :param sigma: param, to be fine-tuned. (a key radius could be right)
    :param word:
    :return:
    """
    btm = 0
    for idx, i in enumerate(remaining_word_candidate):
        new_sigma = sigma
        gamma = 2.0
        if t >= fitts_time_dict[i]:
            new_sigma = sigma
        else:
            new_sigma = sigma * ( 1 + gamma * math.log(t/fitts_time_dict[i]))
        btm += calc_p_x(new_sigma, remaining_word_dist[idx])
    if btm == 0:
        # raise ValueError("btm is zero!")
        return []
    ans_lis = []
    for idx, i in enumerate(remaining_word_candidate):
        new_sigma = sigma
        gamma = 2.0
        if t >= fitts_time_dict[i]:
            new_sigma = sigma
        else:
            new_sigma = sigma * ( 1 + gamma * math.log(t/fitts_time_dict[i]))
        ans_lis.append(calc_p_x(new_sigma, remaining_word_dist[idx]) / btm)
    return ans_lis


def integrate(remain_shape_lis, remain_shape_dist, remain_loc_lis, remain_loc_dist, sigma, fitts_time_dict, t, gamma):
    # TODO: question: is P's equal to P'l ?
    shape_set = set(remain_shape_lis)
    loc_set = set(remain_loc_lis)
    intersec_set = shape_set & loc_set
    intersec_shape_lis = []
    intersec_shape_dist = []
    intersec_loc_lis = []
    intersec_loc_dist = []
    for i in intersec_set:
        intersec_shape_lis.append(i)
        intersec_shape_dist.append(remain_shape_dist[remain_shape_lis.index(i)])
        intersec_loc_lis.append(i)
        intersec_loc_dist.append(remain_loc_dist[remain_loc_lis.index(i)])
    btm = 0

    '''for i in intersec_loc_lis:
        btm += calc_word_prob(intersec_loc_lis, intersec_loc_dist, sigma, i) * \
        calc_word_prob(intersec_shape_lis, intersec_shape_dist, sigma, i)'''

    loc_prob_lis = calc_word_prob(intersec_loc_lis, intersec_loc_dist, sigma, fitts_time_dict, t, gamma)
    shape_prob_lis = calc_word_prob(intersec_shape_lis, intersec_shape_dist, sigma, fitts_time_dict, t, gamma)
    for i in range(len(intersec_loc_lis)):
        btm += loc_prob_lis[i] * shape_prob_lis[i]

    if btm == 0:
        # raise ValueError("integrate error.")
        return []
    score_lis_for_debug = []

    '''for i in intersec_loc_lis:
        # score = calc_word_prob(intersec_loc_lis, intersec_loc_dist, sigma, i) * calc_word_prob(intersec_shape_lis, intersec_shape_dist, sigma, i) / btm
        score_lis_for_debug.append(score)'''

    for i in range(len(intersec_loc_lis)):
        score_lis_for_debug.append(loc_prob_lis[i] * shape_prob_lis[i] / btm)

    data = [(score, word) for score, word in zip(score_lis_for_debug, intersec_loc_lis)]
    data.sort()
    ans_lis = [word for score, word in data]
    ans_lis.reverse()
    return ans_lis
