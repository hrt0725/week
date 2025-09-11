import os
import time

import requests


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"函数 {func.__name__} 运行时间: {end_time - start_time:.7f} 秒")
        return result

    return wrapper


def add_more(func):
    def wrapper(*args, **kwargs):
        print("{}函数开始调用".format(func.__name__))
        result = func(*args, **kwargs)
        print("{}函数执行完毕，结果：{}".format(func.__name__, result))
        return result

    return wrapper


def runNum(number):
    def runNum_(func):
        def wrapper(*args, **kwargs):
            for i in range(number):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return runNum_


# @add_more
# @timer
@runNum(2)
def add(numA, numB):
    result = numA + numB
    print(result)
    return result


if __name__ == "__main__":
    # url = "http://api.yesapi.net/api/App/User/Login"
    # params = {
    #     "app_key": "6CF084D9775F94D57C8A0D698DAD5DB0",
    #     "username": "tom",
    #     "password": "202cb962ac59075b964b07152d234b70"
    # }
    # print(requests.get(url, params).json())

    try:
        int("2w3")
    except TypeError as te:
        print(te)