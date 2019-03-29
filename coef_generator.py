from __future__ import print_function
from __future__ import division
from __future__ import absolute_import


def coef_generator_vuture(N):
    """
    Participants in a pilot study felt more precise in the
        starting location of the word than in the rest of the word
    :param N: number of points, same shape as return list
    :return: coef_list
    """
    mid = 1 / N
    if N > 2:
        N -= 1
        coef_lis = [mid + 0.05]
        tmp = 1 - mid - 0.05
        for i in range(N):
            coef_lis.append(tmp / (N - 1))
    elif N == 2:
        coef_lis = [0.7, 0.3]
    else:
        coef_lis = [1]
    return coef_lis


def coef_generator_shark(N, x):
    """
    :param N: the number of sampling points in the patterns
    :param x: is the weight of the middile point
    :return: coef_lis
    Nx + 1 / 4 * (N^2 - 1) * y = 1 (N mod 2 == 0)
    Nx + 1 / 4 * (N - 2) * N * y = 1 (N mod 2 != 0)
    """
    coef_lis = []
    if N % 2 != 0:
        mid = (N + 1) / 2
        for i in range(1, int(mid) + 1):
            y = (4 - 4 * N * x) / (N * N - 1)
            if y < 0:
                raise ValueError('x is too big.')
            ans = x + (N - 1) / 2 * y - (i - 1) * y
            coef_lis.append(ans)
        for idx, i in enumerate(coef_lis[::-1]):
            if idx == 0:
                continue
            else:
                coef_lis.append(i)
    else:
        mid = N / 2
        for i in range(1, int(mid) + 1):
            y = (4 - 4 * N * x) / (N * (N - 2))
            if y < 0:
                raise ValueError('x is too big.')
            ans = x + (N / 2 - 1) * y - (i - 1) * y
            coef_lis.append(ans)
        for i in coef_lis[::-1]:
            coef_lis.append(i)
    return coef_lis
