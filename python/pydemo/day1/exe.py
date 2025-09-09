import os


def exe_1():
    print("1.回文")
    inputStr = input("输入文字:")
    list1 = list(inputStr)
    list1.reverse()
    resultStr = "".join(list1)
    if resultStr == inputStr:
        print("你输入的是回文字符串")
    else:
        print("你输入的不是回文字符串")


def exe_2():
    print("2.元音字母数")
    inputStr = input("输入文字:").lower()
    number = 0
    word = ['a', 'e', 'i', 'o', 'u']
    for item in word:
        number += inputStr.count(item)
    print("音字母数:{}".format(number))


def exe_3():
    print("3.字符替换为'_'")
    inputStr = input("输入文字:")
    resultStr = inputStr.strip().replace(" ", "_")
    print(resultStr)


def exe_4():
    print("4.首字母大写")
    inputStr = input("输入文字:")
    strList = inputStr.split()
    resultList = []
    for strItem in strList:
        resultList.append(strItem.capitalize())
    print(" ".join(resultList))


def exe_5():
    print("5.判断字符")
    char1 = input("输入单个字符:")
    wordType = ""
    if char1[0].isdigit():
        wordType = "数字"
    elif char1[0].isupper():
        wordType = "大写字母"
    elif char1[0].islower():
        wordType = "小写字母"
    print("‘{}’是{}".format(char1[0], wordType))


def exe_6():
    print("6.列表转集合，不适用set()")
    nums = [1, 2, 2, 3, 4, 4, 5]
    newNums = []
    for num in nums:
        try:
            newNums.index(num)
        except:
            newNums.append(num)
    print(newNums)


def exe_7():
    print("7.筛选偶数")
    numbers = [3, 7, 12, 19, 24, 30]
    resultList = []
    for num in numbers:
        if num % 2 == 0:
            resultList.append(num)
    print("原列表：{}".format(numbers))
    print("偶数列表：{}".format(resultList))


def exe_8():
    print("8.反转列表")
    fruits = ["apple", "banana", "cherry"]
    resultFruits = fruits.copy()
    resultFruits.reverse()
    print("原列表：{}".format(fruits))
    print("反转列表：{}".format(resultFruits))


def exe_9():
    print("9.累加成绩")
    scores = [85, 92, 78, 90, 88]
    sum = 0
    for item in scores:
        sum += item
    print("和为:" + str(sum))


def exe_10():
    print("10.元组拆分")
    person = ("张三", 25, "男", "工程师")
    name, age, gender, occP = person
    print("姓名：{}，年龄：{}，性别：{}，职业：{}".format(name, age, gender, occP))


def exe_11():
    print("11.统计颜色‘red’次数")
    colors = ("red", "blue", "red", "green", "blue", "red")
    redCount = colors.count('red')
    print("'red'出现{}次".format(redCount))


def exe_12():
    print("12.元组转列表转元组")
    nums_tuple = (1, 3, 5, 7)
    numsList = list(nums_tuple)
    numsList.append(9)
    numsTupleNew = tuple(numsList)
    print(numsTupleNew)


def exe_13():
    print("13.遍历字典")
    student = {"name": "李四", "age": 20, "score": 89, "major": "计算机"}
    for item in student.items():
        print(item)


def exe_14():
    print("14.筛选大于80的成绩保存到新字典")
    scores = {"语文": 75, "数学": 95, "英语": 80, "物理": 60}
    result = {}
    for item in scores.items():
        if int(item[1]) > 80:
            result.setdefault(item[0], item[1])
    print("原列表：{}".format(scores))
    print("新列表：{}".format(result))


def exe_15():
    print("15.字典合并和去重")
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    newDict = {}
    for dt1Item in dict1.items():
        for dt2Item in dict2.items():
            if dt2Item[0] != dt1Item[0]:
                newDict.setdefault(dt1Item[0], dt1Item[1])
                newDict.setdefault(dt2Item[0], dt2Item[1])
            else:
                newDict.setdefault(dt2Item[0], dt2Item[1])
    print("字典1：{}".format(dict1))
    print("字典2：{}".format(dict2))
    print("新的字典：{}".format(newDict))

def exe_15_2():
    print("15.2 字典合并和去重")
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    newDict = {}
    newDict.update(dict1)
    newDict.update(dict2)
    print("字典1：{}".format(dict1))
    print("字典2：{}".format(dict2))
    print("新的字典：{}".format(newDict))

def exe_16():
    print("16.字典键值获取")
    user_info = {"username": "alice", "email": "alice@xxx.com"}
    if user_info.get("age") is None:
        user_info.setdefault("age", 18)
    print("添加后：{}".format(user_info))


def exe_17():
    print("17.九九乘法表")
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("{}x{}={}\t".format(j, i, i * j), end='')
        print()


def exe_18():
    print("18.成绩评级")
    student_scores = [("小明", 75), ("小红", 92), ("小刚", 58), ("小丽", 88)]
    for scoreItem in student_scores:
        if scoreItem[1] >= 90:
            grade = "A"
        elif scoreItem[1] >= 80:
            grade = "B"
        elif scoreItem[1] >= 70:
            grade = "C"
        else:
            grade = "D"
        print("{}:分数{}，等级{}".format(scoreItem[0], scoreItem[1], grade))


def exe_19():
    print("19.判断密码")
    password = input("输入你的密码：").strip()
    numCount = 0
    upWordCount = 0
    if len(password) >= 8:
        for word in password:
            if 0 <= ord(word) <= 57:
                numCount += 1
            if 65 <= ord(word) <= 90:
                upWordCount += 1
        if numCount < 1 or upWordCount < 1:
            print("密码无效：未包含至少1个数字和1个大写字母")
        else:
            print("密码有效")
    else:
        print("密码无效：长度不足8位")


def exe_20():
    print("20.嵌套列表元素求和")
    nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    sum = 0
    for nestedItem in nested_list:
        for item in nestedItem:
            sum += item
    print("原列表:{}".format(nested_list))
    print("元素和为：{}".format(sum))


def showTip():
    print('🤣👉：not find\nfunctions(don`t input:\'exe_\'):')
    globalsCopy = globals().copy()
    for item in globalsCopy.keys():
        if item.startswith("exe_"):
            print(item + "\t", end='')
    print("\n\n🤓:You can input q(quit) c(clear)")


if __name__ == "__main__":
    while True:
        opt = input("🚀Your Operation:")
        if opt == "q" or opt == "quit":
            break
        if opt == "c" or opt == "clear":
            os.system("cls")
            continue
        try:
            globals()[f"exe_{opt}"]()
        except:
            showTip()
