from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from calc_delta import calc_delta
from coef_generator import coef_generator_shark, coef_generator_vuture


def calc_x_l(N, u, t, r, coef):
    """
    :param N: number of re-sampled points
    :param u: unknown input trace (list)
    :param t: ideal trace (list)
    :param r: radius of an alphabetical key
    :return:
    """
    x_l = 0
    for i in range(N):
        x_l += coef[i] * calc_delta(i, u, t, N, r)
    return x_l


def calc_word_dist_lis(word_lis, N, template_points_dict, unknown_points, r):
    # TODO: template_points_lis is a dict. template_points_lis['word']
    # TODO: so slow
    word_dist_lis = []
    coef = coef_generator_vuture(N)
    for i in word_lis:
        word_dist_lis.append(calc_x_l(N, unknown_points, template_points_dict[i], r, coef))
    return word_dist_lis
