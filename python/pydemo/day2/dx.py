class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__mobile = ""

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def mobile(self):
        return self.__mobile

    @mobile.setter
    def mobile(self, mobile):
        if len(str(mobile)) == 11:
            self.__mobile = str(mobile)
        else:
            raise ValueError("需要11位号码")
        try:
            int(str(mobile))
        except:
            raise ValueError("需要纯数字")

    def introduce(self):
        print("My name is {} and {} years old".format(self.__name, self.__age))
        return self

    def eat(self, foodName):
        print("I like eat {}".format(foodName))
        return self

    def call(self):
        print("我的电话是{}，你可以随时打给我".format(self.mobile))


class Animal:
    def __init__(self, name, eyeNum, moveMethod, local):
        self.name = name
        self.eyeNum = eyeNum
        self.moveMethod = moveMethod
        self.local = local

    def introduce(self):
        print("I`m a {}.I have {} eye and live in {}".format(self.name, self.eyeNum, self.local))

    def move(self):
        print("I use {} move".format(self.moveMethod))


class Vehicle:
    def __init__(self, name, brand, wheelNum, local):
        self.name = name
        self.brand = brand
        self.wheelNum = wheelNum
        self.local = local

    def introduce(self):
        print("这是{}品牌的{}，有{}个轮子".format(self.brand, self.name, self.wheelNum),end='')

    def run(self):
        print("我正在{}运行".format(self.local),end='')


if __name__ == "__main__":
    tom = Person('Tom', 18)
    tom.mobile = 18754155651
    tom.call()
