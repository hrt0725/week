# -*- coding: utf-8 -*-
# @Time    : 2025/9/23 15:42
# @Author  : Lan
# @File    : test_demo_skip.py
# @Software: PyCharm
# @Description :
from pickle import FALSE

import pytest


class TestDemoSkip:
    @pytest.mark.skip()
    def test_add(self):
        print("add")
        assert 1 + 3 == 4

    def test_sub(self):
        print("sub")
        assert 1 - 1 == 0

    @pytest.mark.xfail(condition=False, reason="预期成功的")  # 条件不成立，预期成功，assert结果断言成功
    def test_mul(self):
        print("mul")
        assert 2 * 6 == 12

    @pytest.mark.xfail(condition=True, reason="预期失败的")  # 条件成立，预期失败，assert断言结果失败，
    def test_div(self):
        print("div")
        assert 6 / 2 == 1


if __name__ == '__main__':
    pytest.main()
