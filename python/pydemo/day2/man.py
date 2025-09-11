from day2.dx import Person, Animal


class Man(Person):
    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.job = job

    def work(self, name):
        print("我的职业是{}，我正在{}".format(self.job, name))

    def eat(self, foodName):
        print("我是一个男人，我爱吃{}".format(foodName))

    def introduce(self):
        print("我的名字是{}，我今年{}岁了".format(self.name, self.age))

def introduce(p):
    p.introduce()

if __name__ == "__main__":
    man1 = Man("Thr", 15, "老师")
    man1.introduce()
    man1.mobile = "12345678511"
    man1.call()
    man1.work("摸鱼")
    man1.eat("水泥")


    p1 = Person("人1",12)

    introduce(p1)
    introduce(man1)




