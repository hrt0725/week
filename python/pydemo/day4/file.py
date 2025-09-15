import csv


def write():
    with open("aa.txt", "a+") as file:
        for i in range(5):
            file.write("hello world\n")


def read():
    with open("aa.txt", "r") as file:
        print(file.readlines())
        while True:
            lineContent = file.readline()
            print(lineContent, end="")
            if not lineContent:
                break


def write_csv(filename, head, data, mode="w"):
    with open(filename, mode, encoding="utf-8", newline="") as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(head)
        csvWriter.writerows(data)


def read_csv():
    with open("aa.csv", "r", encoding="utf-8", newline="") as csvFile:
        csvReader = csv.reader(csvFile)
        head = next(csvReader)
        print(head)
        for row in csvReader:
            print(row)


def write_dict_csv():
    with open("aa.csv", "w", encoding="utf-8", newline="") as csvFile:
        head = ["name", "age", "sex"]
        data = [
            {"name": "tom", "age": 15, "sex": "man"},
            {"name": "jerry", "age": 19, "sex": "man"},
            {"name": "luck", "age": 20, "sex": "woman"}
        ]
        csvDictWriter = csv.DictWriter(csvFile, head)
        csvDictWriter.writeheader()
        csvDictWriter.writerows(data)


def read_dict_csv():
    with open("aa.csv", "r", encoding="utf-8", newline="") as csvFile:
        csvDictReader = csv.DictReader(csvFile)
        for row in csvDictReader:
            print(row)

if __name__ == "__main__":
    head = ["测试编号", "测试标题", "测试模块"]
    data = [
        ["test_tc_01", "用户登录成功", "用户登录"],
        ["test_tc_02", "用户登录失败", "用户登录"],
        ["test_tc_03", "用户名为空", "用户登录"],
        ["test_tc_04", "密码为空", "用户登录"],
    ]
    # write_csv("aa.csv", head, data, "w")
    # read_csv()
    read_dict_csv()
