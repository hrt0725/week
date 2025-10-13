##### **Python版本**

* Python 2.x
* Python 3.x 主流
* [https://docs.python.org/zh-cn/3/](https://docs.python.org/zh-cn/3/)

##### **Python特点**

* 简洁易懂-语法规范
* 跨平台-支持Windows、Linux、Mac
* 多编程范式-面向对象，函数式编程
* 丰富的库-内置库(OS，time，Requests)、三方库(Selenium，pytest，pandas，numpy)
* 解释型和动态性-无需显式声明变量，代码逐行解释；

##### **应用领域**

* Web开发：Flask轻量级，Django重量级；
* 大数据处理-数据爬虫，pandas，numpy
* 机器学习人工智能：算法开发、神经网络、大模型sckit-learn，PyTorch
* 自动化测试：Web自动化，接口自动化，Selenium，Requests，pytest;
* 其他领域：游戏开发Pygame，教育，物联网；

##### **基础**

###### **Python环境**

**Python安装**

* Python官网下载（Python.org） Python 3.10+版本
* 环境变量：安装路径添加到系统环境变量；
  * C:\Python313
  * C:\Python313\Scripts
* 验证安装：`Python -v`

###### Python IDE工具

* PyCharm、VSCode

###### **Python输入输出**

* 输出 print
  ```python
  print("hello world!")
  ```
* 输入 input
  ```python
  name=input("请输入内容")
  print(name)
  ```

##### **python变量和数据类型**

###### **python变量**

* 变量定义：`name="harry"`
* 变量命名规范

  * 量名称有字母,数值，下划线组合；不能单独用数字，或以数字开头；
  * 变量命名，由英文单词构成，避免使用拼英，见其名知其意
  * 驼峰命名：多个单词组合，由下划线拼接，或者其他单词首字母大写；userAddress；
  * 变量区分大小写；
  * 不使用系统自带的关键字，数据类型，内置函数等命名；比如：import，if，while；
  * 变量的作用域
    * 遵守LEGB规则
    * L：local局部范围：作用范围在函数内部使用；
    * E：嵌套，函数嵌套函数；外部函数定义变量，可以在内部函数中使用；
    * G：global全局变量，在一个.py中使用；
    * B：builtln，python内置使用；
* ###### 变量赋值


  * 常规赋值：
    * `name="tom"`
    * `name="张三",age=18`
  * 多元赋值：
    * `x,y,z=18,26,36`
    * `x=y=z=20`
  * 查看变量存储空间：id(变量名)
    * 短整数范围在-5 - 256内的整数，内存中存储空间空用；

###### **数据类型：**

* 整数：`age=18`
* 浮点型：`price=13.99`
* 复数：`a=5+6j`；实部：a.real；虚部：a.imag

**类型转换：int()  float()**

* x=int(15.8)   #15
* y=float(51)   #51.0
* z=str(123)     #'123'

###### **算术运算**

* 加减乘除：`+  -  *  /  %  //  **`
* 加减乘除赋值：`+=  -=  *=  /=  %=`

###### **字符串类型（str）**

* name="harry"  #双引号
* address='四川成都'
* 字符串拼接：'123'+"34"     #'12334'
* `*` ：字符串重复   `"hello" * 2`  # hellohello
* 字符串转义
  * `\`转义特殊字符\t制表空格\n换行
  * r：转义路径 `print(r"D:\aa\bb\cc.png")`
* 字符串包含in/not in：`"harry" in "harry123"  #True`
* 字符串函数：
  * len(s)：字符串长度
  * str.count('a')：统计字符串的次数
  * str.find('a')：查找字符串，返回索引位置
  * str.strip()：去除字符串两边空格
  * str.replace('old','new')：字符串替换
  * str.startswidth('http')：查找字符串前缀，返回布尔值
  * str.endswidth('.png')：查找字符串后缀，返回布尔值
  * str.split(',')：字符串分割，返回分割后的列表
  * "".join([])：对列表值进行拼接
  * str[ start : end : step ]：字符串截取

###### **布尔类型（bool）**

* 判断逻辑真假：True，False；首字母大写
* `isTrue=True`

###### **空值None Type**

* 表示为空或无结果；不同于：""，0，[]
* 判断需要使用is判断
  * `name=None`
  * `name is None   #返回True`
  * `name=''`
  * `name is None  #返回False`

###### **列表list**

* 定义： `user_list=["harry","tom","jerry"]`
* 列表使用：
  * 索引位置取值；
  * 切片取值
  * 常用函数：
    * 添加数据
      * lst.insert(index,value)：插入元素到指定位置；
      * lst.append(object)：把元素(单个值或列表)追加到列表末尾；
      * lst.extentd(lst)：把列表中的元素加入到原列表；
      * 列表相加：list1+list2   两个列表组合为一个列表；
    * 移除数据
      * lst.remove(value)：移除匹配到的第一个元素；
      * lst.pop(index)：移除指定位置的元素；
      * lst.clear()：清空列表所有数据；
    * 获取长度、最大值、最小值
      * len(lst)
      * max(lst)
      * min(lst)
    * 列表排序、反序列
      * lst.sort()：升序排列
      * lst.reverse()：列表反序列
    * 列表的复制
      * lst.copy()

###### **元组tuple**

* 元素定义：`tup=(1,2,3)`
* 元组使用：`tup[1]`
* 类型转换：`lst=list(tup)；tup=tuple(lst)`

###### **字典dict**

* 字典定义：`userinfo={"name":"harry","age":18,"address":"四川成都"}`
* 字典常用方法
  * 获取字典的长度：`len(dict)`
  * 判断key是否存在：`key in dict`
  * 获取字典的值：
    * userInfo["key"]
    * userInfo.get("key")
    * userInfo.setdefault("key",value)：key不存在则添加进去；
  * 字典更新：
    * userInfo["key"]=value
    * userInfo.setdefault("key",value)：key不存在则加入；
    * userInfo.updata(dit)：把字典更新进去；
    * userInfo.copy()：复制字典
  * 字典删除：
    * userInfo.pop("key")：删除元素key
    * upderInfo.clear()：清空所有元素
  * 字典遍历
    * dict.items()：遍历字典每一项
    * dict.key()：遍历字典的每个键
    * dict.values()：遍历字典的值

###### **集合set**

* 定义集合：se=set(),se={1,2,3,4}
* 常见方法
  * 获取长度len(set)
  * 添加数据：
    * se.add(value)  #添加值到集合
    * se.update([])   #添加列表值到集合
    * se.copy()           #复制数据
  * 删除数据：
    * se.pop()             #随机删除数据
    * se.remove()     #删除指定值
    * se.clear()           #清空数据

##### **流程控制语句**

###### **语法规范**：

* 代码注释
  * 单行注释：#
  * 多行注释：三引号
    ''' 多行注释 '''
    """ 多行注释  """
* 代码缩进
  * 使用Tab键把同一层级代码的缩进；一般外层和内层保持一个缩进；左对齐；
  * 代码行结束不用加分号，同一行中，不同逻辑需要用分号分割；

###### **if条件判断**

* if....elif....else
* if....
* if....else....
* 示例
  ```python
  score = int(input("输入你的成绩："))
  if score >= 0 and score <= 100:
      print("成绩合法")
      if score >= 90:
          print("A")
      elif score >= 80:
          print("B")
      elif score >= 70:
          print("C")
      elif score >= 60:
          print("D")
      else:
          print("E")
  else:
      print("成绩不合法")
  ```

###### **for循环**

* for.....in

```python
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
```

* for.....else
  ```python
  #for....else
  users={"name":"harry","age":18}
  user_li={"name":"harry"}
  for user in users:
  if users[user]==user_li['name']:
  print("找到了",user)
  break
  else:
  print（"未找到")
  ```

###### **while循环**

* while....:

  ```python
  i=1
  while i<10:
      print(i)
      i+=1
  ```
* match...case条件选择

  ```python
  va = input("input>")
      match va:
          case "+":
              print("加")
          case "-":
              print("减")
          case _:
              print("其它")
  ```

###### **注意事项**

* 先注释再编程
* 先理思路，在编程中寻求解决方案；
* 编程细节要注意：输入数据去空格，数据类型要转换，变量声明要规范;
* 代码完成要优化：优化代码运算逻辑，代码的行数，不必要的调试信息；
* 重复性的代码要封装：独立的代码块封装为函数，类提高代码的复用率；

##### **函数**

###### **基本函数**

###### **函数的定义**

* def   func(agr):
* 函数名称：
  * 蛇形命名（func_add）
  * 驼峰命名（funcAdd）
  * \_\_func_add 下划线开头
  * pass进行内容占位
  * return 返回值
  * 参数
    * 位置参数
    * 默认参数
    * 关键字参数
    * 可变参数
    * 可变关键字参数
    * 优先级：位置参数>关键字参数>默认值参数>可变参数>可变关键字参数

###### **函数调用：func()**

###### **匿名函数 lanbda**

* 定义：无需声明函数名称，直接介绍参数进行运算返回结果

  * result = lambda 参数1,参数2: 表达式/调用的函数

  ```Python
  result = lambda x, y: x + y
  print(result(1, 2))
  ```

###### **列表推导**

* 定义：对一个序列（列表、元组、字典）遍历，数据逐个处理后生成新的列表
* 语法格式
  `result = [ 表达式 for i in 列表 if 条件 ]`
* 实例
  ```Python
  nums = [3, 7, 12, 19, 24, 30]
  new_nums = [num for num in nums if num % 2 == 0]
  print(new_nums)
  ```

###### **高阶函数**

* 定义：把一个函数作为参数传递，或者把函数作为结果进行return；
* 系统内置的高阶函数
* map(func,iter)：对迭代对象进行逐一处理，**数据处理**
  ```python
  result = list(map(lambda x: x + 1, [1, 2, 3, 4, 5]))
  print(result)
  ```
* filter(func,iter)：对迭代对象进行**数据筛选**
  ```python
  result = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
  print(result)
  ```

##### **面向对象**

###### **类class**

* 定义：具有相同外部特征或者动作行为的个体的集合；
* 属性：用来描述类的外在静态特征；
* 方法：用来描述类的动作行为；

###### **对象**

* 定义：类中具体的个体；具备类的属性和方法；通过类的实例化生成；
  ```python
  class Person:
      def __init__(self, name, age):
          self.__name = name
          self.__age = age

      def say(self):
          print("My name is {} and {} years old".format(self.__name, self.__age))
          return self

      def eat(self, foodName):
          print("I like eat {}".format(foodName))
          return self

  if __name__ == "__main__":
      tom = Person('Tom', 18)
      tom.say().eat("樱桃")
      jerry = Person('jerry', 25)
      jerry.say().eat("香蕉")
  ```

###### 封装

* 定义：把类的属性数据或方法操作进行处理，实现安全访问，隐私处理等隐私处理
* 属性封装
  * 构造函数 `__init__`通过 `__`对属性设置私密属性,禁止外部访问，通过添加 `@property`装饰器
    ```python
    class Person:
        def __init__(self, name, age):
            self.__name = name
            self.__age = age
            self.__mobile = ""

        @property
        def mobile(self):
            return self.__mobile

        @mobile.setter
        def mobile(self, mobile):
             self.__mobile = str(mobile)
    ```
* 方法封装
  * 通过在方法名前面添加 `__`设置私有方法，禁止外部调用；
  * 对外访问其它公共方法，方法内部调用私有方法；

###### 继承

* 定义：子类继承父类的属性和方法，无需单独定义；也可以单独定义属性和方法；
* 定义子类后括号中引用父类，可以继承单个类，也可以继承多个类；
  ```python
  from day2.dx import Person

  class Man(Person):
      pass
      def work(self,name):
          print("working:".format(name))
  ```
* 继承属性：
  * 子类不添加构造函数二init_方法，默认继承父类所有的属性
  * 子类添加特有的属性，定义构造函数时，需使用super()引用父类的构造函数；
    `super().__init__(父类的属性)`
  * 方法继承：默认直接继承父类的所有方法；
  * 方法重写：对父类的方法，子类中定义一个同名的方法，进行逻辑的修改；

###### **多态**

* 定义：基于类继承的方法重写的基础之上，建立一个统一的对外接口方法，实现不同类的对象，调用时实现各自的业务逻辑；

  ```python
  def people_sleep(people):  # people是类的对象
      people.sleep()  # 调用子类重写的方法

  p = Person()
  b = Boy()
  m = Male()
  # 接口调用
  people_sleep(p)
  people_sleep(b)
  people_sleep(m)
  ```

###### **装饰器**

* 定义：在不改变原有函数代码逻辑的基础上，单独定义一个函数，实现对原有函数的功能附加，比如日志打印处理，数据处理，性能执行时间的测算等;
* 装饰器本质是一个函数之间互相调用的高阶函数，包括有参和无参；

  ```python
  def runNum(number):
      def runNum_(func):
          def wrapper(*args, **kwargs):
              for i in range(number):
                  result = func(*args, **kwargs)
              return result
          return wrapper
      return runNum_
  ```
* 装饰器调用

  ```python
  @runNum(2)
  def add(numA, numB):
      result = numA + numB
      print(result)
      return result
  ```

##### **模块**

* 包：package
* 库：library
* 类：class
* 方法：method
* 包含关系：package>library>class>method

###### **内置库**

* os
* sys
* time
* request

###### **三方库**

* selenium
* pytest
* numpy
* flask

**模块的引用：**

* 内置的库

  ```python
  import os
  import time，os
  ```
* 三方的库

  * 需要先安装：`pip install selenium`
  * 引用：
    `from selenium import webdriver`
* 自定义的库
  `from package.filename import ClassName`
  `from package import class.method`
  `from package.filename.class import method`

##### **异常处理**

###### **异常捕获**

* 定义：代码逻辑中可能存在的异常错误进行接收处理，易于用户理解和接受，避免出现崩溃闪退等不可接受的情况；
* try-except-else
  ```python
  try:
      a,b = 6,0
      result = a/b
      print(result)
  except ZeroDivisionError as e:
      print("除数不能为0")
  ```

###### **异常抛出**

* 定义：在业务处理过程中存在错，使用raise抛出错误，便于定位；
* 使用Python内置的错误类型：TypeError，ValueError

##### **文件读写**

* 常见文件读写：text，csv，excel

###### **test文件读写**

* file = open(filename.mode,encoding='utf-8')
* with open() as file:

###### **文件写入**

* file.write("www")
* file.writelines([])
* file.close()：文件关闭

###### **文件读取**

* file.read()：读取全部内容
* file.radline()：读取一行内容
* file.readlines()：读取所有行，返回列表
* file.close()：文件关闭

###### **CSV文件读取**

* 列表形式的读写

  ```python
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
  ```
* 字典形式的读写

  ```python
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
  ```
* pandas读写csv

  ```python
  import pandas as pd

  data = {
      "name": ["张飞", "关羽", "刘备"],
      "age": [32, 36, 45],
      "province": ["四川阆中", "山西", "河北"],
      "nickname": ["张翼德", "关云长", "刘玄德"]
  }
  df = pd.DataFrame(data)
  df.to_csv("pandas_to_csv.csv", index=False, encoding="utf-8")

  print(pd.read_csv("pandas_to_csv.csv"))
  ```

###### **Excel文件读写**

* 安装三方库openpyxl、pandas
  `pip install openpyxl pandas`
* pandas
