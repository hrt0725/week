# -*- coding: utf-8 -*-
# @Time    : 2025/9/28 16:22
# @Author  : Lan
# @File    : test_allure_goods.py
# @Software: PyCharm
# @Description :
import allure
import pytest


@allure.feature("allure-商品模块")
class TestAllureGoods:
    @allure.link("http://baidu.com")
    @allure.story("allure-商品添加")
    @allure.title("allure-商品添加成功")
    @pytest.mark.parametrize("goodsName,price", zip(["连衣裙", "牛仔裤"], ["123", "444"]))
    def test_allure_goods_add_success(self, goodsName, price):
        print("goodsName:{};price{}".format(goodsName, price))
        assert 2 == 2

    @allure.story("allure-商品添加")
    @allure.title("allure-商品添加失败")
    @pytest.mark.parametrize("goodsName,price", zip(["冲锋衣", "大衣"], ["324", "654"]))
    def test_allure_goods_add_filed(self, goodsName, price):
        print("goodsName:{};price{}".format(goodsName, price))
        assert 2 == 2

    @allure.story("allure-商品分类添加")
    @allure.title("allure-商品分类添加成功")
    @pytest.mark.parametrize("typename", ["衣服", "裤子"])
    def test_allure_goods_type_add_success(self, typename):
        print("typename:{}".format(typename))
        assert 2 == 2


if __name__ == '__main__':
    pass
