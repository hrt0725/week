**Python版本**

* Python 2.x
* Python 3.x 主流
* [https://docs.python.org/zh-cn/3/](https://docs.python.org/zh-cn/3/)

**Python特点**

* 简洁易懂-语法规范
* 跨平台-支持Windows、Linux、Mac
* 多编程范式-面向对象，函数式编程
* 丰富的库-内置库(OS，time，Requests)、三方库(Selenium，pytest，pandas，numpy)
* 解释型和动态性-无需显式声明变量，代码逐行解释；

**应用领域**

* Web开发：Flask轻量级，Django重量级；
* 大数据处理-数据爬虫，pandas，numpy
* 机器学习人工智能：算法开发、神经网络、大模型sckit-learn，PyTorch
* 自动化测试：Web自动化，接口自动化，Selenium，Requests，pytest;
* 其他领域：游戏开发Pygame，教育，物联网；

**基础**

**Python环境**

**Python安装**

* Python官网下载（Python.org） Python 3.10+版本
* 环境变量：安装路径添加到系统环境变量；
  * C:\Python313
  * C:\Python313\Scripts
* 验证安装：`Python -v`

Python IDE工具

* PyCharm、VSCode

**Python输入输出**

* 输出 print
  ```python
  print("hello world!")
  ```
* 输入 input
  ```python
  name=input("请输入内容")
  print(name)
  ```

**python变量和数据类型**

**python变量**

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
* 变量赋值

  * 常规赋值：
    * `name="tom"`
    * `name="张三",age=18`
  * 多元赋值：
    * `x,y,z=18,26,36`
    * `x=y=z=20`
  * 查看变量存储空间：id(变量名)
    * 短整数范围在-5 - 256内的整数，内存中存储空间空用；

**数据类型：**

* 整数：`age=18`
* 浮点型：`price=13.99`
* 复数：`a=5+6j`；实部：a.real；虚部：a.imag

**类型转换：int()  float()**

* x=int(15.8)   #15
* y=float(51)   #51.0
* z=str(123)     #'123'

**算术运算**

* 加减乘除：`+  -  *  /  %  //  **`
* 加减乘除赋值：`+=  -=  *=  /=  %=`

**字符串类型（str）**

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

**布尔类型（bool）**

* 判断逻辑真假：True，False；首字母大写
* `isTrue=True`

**空值None Type**

* 表示为空或无结果；不同于：""，0，[]
* 判断需要使用is判断
  * `name=None`
  * `name is None   #返回True`
  * `name=''`
  * `name is None  #返回False`

**列表list**

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

**元组tuple**

* 元素定义：`tup=(1,2,3)`
* 元组使用：`tup[1]`
* 类型转换：`lst=list(tup)；tup=tuple(lst)`

**字典dict**

* 字典定义：`userinfo={"name":"harry","age":18,"address":"四川成都"}`
* 字典常用方法
  * 获取字典的长度：`len(dict)`
  * 判断key是否存在：`key in dict`
  * 获取字典的值：
    * userInfo["key"]
    * userInfo.get("key")
    * userInfo.setdefault("key")：key不存在则添加进去；
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

**集合set**

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

**流程控制语句**

**语法规范**：

* 代码注释
  * 单行注释：#
  * 多行注释：三引号
    ''' 多行注释 '''
    """ 多行注释  """
* 代码缩进
  * 使用Tab键把同一层级代码的缩进；一般外层和内层保持一个缩进；左对齐；
  * 代码行结束不用加分号，同一行中，不同逻辑需要用分号分割；

**if条件判断**

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

**for循环**

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

**while循环**

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
