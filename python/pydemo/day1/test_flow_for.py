import unittest

# score = int(input("输入你的成绩："))
# if score >= 0 and score <= 100:
#     print("成绩合法")
#     if score >= 90:
#         print("A")
#     elif score >= 80:
#         print("B")
#     elif score >= 70:
#         print("C")
#     elif score >= 60:
#         print("D")
#     else:
#         print("E")
# else:
#     print("成绩不合法")

#遍历列表
names=['tome','jerry','luck']
i=1
for name in names:
    #print("第"+str(i)+'个用户:'+name)
    print("第{}个用户：{}".format(i,name))
    i+=1

userInfo={
    "name":"tom",
    "age":18,
    "gender":"man",
}
#遍历字典
for key,value in userInfo.items():
    print("{}的值为：{}".format(key,value))

if __name__ == "__main__":
    unittest.main()
