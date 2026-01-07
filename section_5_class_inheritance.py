class Car:
    def __init__(self):
        self.wheel_count = 4
        self.door_count = 2

    def start(self):
        print("started...")

    def drive(self):
        print("driving...")
        
class TankLorry(Car):
    def __init__(self):
        super().__init__() # super(). -> 부모의 어트리뷰트를 모두 안전하게 상속받으며 다음줄에 각각 세부사항을 커스텀으로 덮어쓸 수 있다.
        self.wheel_count = 10
        
    def start(self):
        super().start()
        print("ggggrrrrrrr..")