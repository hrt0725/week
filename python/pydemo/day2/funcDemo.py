# 匿名函数
import time
from functools import wraps

result = lambda x, y: x + y
print(result(1, 2))

# 列表推导
# res = [ 表达式 for i in [] if 条件 ]

nums = [3, 7, 12, 19, 24, 30]
new_nums = [num for num in nums if num % 2 == 0]
print(new_nums)


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"函数 {func.__name__} 运行时间: {end_time - start_time:.7f} 秒")
        return result
    return wrapper


@timer
def exe_17():
    print("17.九九乘法表")
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("{}x{}={}\t".format(j, i, i * j), end='')
        print()


# 九九乘法表
@timer
def jj1():
    [[print("{}x{}={}\t".format(j, i, i * j), end='') for j in range(1, i + 1)] and print() for i in range(1, 10)]


# jj1()
# exe_17()

# map(func,iter) 对迭代数据处理，return
result = list(map(lambda x: x + 1, [1, 2, 3, 4, 5]))
print(result)


def test_add(a):
    return a * 10


result = list(map(test_add, [1, 2, 3, 4, 5]))
print(result)

# filter(func,iter) 数据筛选
result = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
print(result)
