from day2.dx import Animal


class Dog(Animal):

    def __init__(self, name, eyeNum, moveMethod, local):
        super().__init__(name, eyeNum, moveMethod, local)
        self.__footNum = 4

    def introduce(self):
        print("他的名字是{}，有{}只眼睛，生活在{}".format(self.name, self.eyeNum, self.local))

    def move(self):
        print("我使用{}条{}运动".format(self.__footNum,self.moveMethod))
    


if __name__ == "__main__":
    dog1 = Dog("哈士奇", 2, "腿", "陆地")
    dog1.introduce()
    dog1.move()
