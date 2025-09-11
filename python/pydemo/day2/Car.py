from day2.dx import Vehicle


class Car(Vehicle):
    def __init__(self, name, brand, driveMethod, maxSpeed):
        super().__init__(name, brand, 4, "陆地")
        self.driveMethod = driveMethod
        self.maxSpeed = maxSpeed

    def introduce(self):
        super().introduce()
        print(",是一辆{}车,最高时速{}km/h".format(self.driveMethod, self.maxSpeed))

    def run(self, speed=0):
        super().run()
        print(",当前时速：{}km/h".format(speed))



if __name__ == "__main__":
    car1 = Car("AMG GT BS", "benz", "四驱", "500")
    car1.introduce()
    car1.run(210)

    car1 = Car("AMG one", "benz", "四驱", "500")
    car1.introduce()
    car1.run(210)
