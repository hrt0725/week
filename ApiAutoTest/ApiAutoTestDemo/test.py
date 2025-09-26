# -*- coding: utf-8 -*-
# @Time    : 2025/9/25 10:22
# @Author  : Lan
# @File    : test.py
# @Software: PyCharm
# @Description :
import itertools


def get_all_subsets(input_set):
    """返回集合的所有子集"""
    elements = list(input_set)
    subsets = []
    # 生成所有可能的子集大小（从0到集合长度）
    for r in range(len(elements) + 1):
        # 生成大小为r的所有组合
        for combo in itertools.combinations(elements, r):
            subsets.append(set(combo))
    return subsets


def t_get_all_subsets():
    my_set = {("tom", "123"), ("jerry", "333"), ("luck", "012")}
    subsets = get_all_subsets(my_set)
    print("所有子集:")
    for subset in subsets:
        print(list(subset))


if __name__ == '__main__':
    pass
