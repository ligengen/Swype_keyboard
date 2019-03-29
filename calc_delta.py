from __future__ import division
from __future__ import print_function
from __future__ import absolute_import


def calc_d(pi, q, N):
    """
    :param pi:
    :param q:
    :return:
    """
    min_val = 99999999999999999999999999999999999999999999999999999
    for i in range(N):
        # if len(q) not == N:
        #     print("fuck")
        qi = q[i]
        norm = (pi[0] - qi[0]) ** 2 + (pi[1] - qi[1]) ** 2
        if norm < min_val:
            min_val = norm
    return min_val ** 0.5


def calc_big_d(p, q, r, N):
    big_d = 0
    for i in range(N):
        big_d += max(calc_d(p[i], q, N) - r, 0)
    return big_d


def calc_delta(i, u, t, N, r):
    if calc_big_d(u, t, r, N) == 0 and calc_big_d(t, u, r, N) == 0:
        return 0
    else:
        return ((u[i][0] - t[i][0]) ** 2 + (u[i][1] - t[i][1]) ** 2) ** 0.5

