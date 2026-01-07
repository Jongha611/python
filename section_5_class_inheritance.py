class Car:
    def __init__(self):
        self.wheel_count = 4
        self.door_count = 2

    def start(self):
        print("started...")

    def drive(self):
        print("driving...")
        

# 이 챕터는 부모클래스와 자식클랫스 즉 클래스간의 상속에 관한 논의이다. 클래스-함수 관계는 논의하지 않는다.
# 만약 자식클래스가 상속을 받고 똑같은 함수를 만들지 않으면 부모 클래스의 함수들을 모두 상속받는다.
# 그러나 __init__() 등 부모클래스에 존재하는 함수를 새로 만들면, 부모의 __init__은 자동으로 호출되지 않고 독립된 __init__을 갖게 된다.
# 이 때, super().메서드() -> 원래 자동으로 호출되지 않는 부모의 속성들을 모두 상속받되, 안전하게 추가나 수정도 가할 수 있게 된다.
# 결국 **super()**라는 키워드는 클래스 상속 관계에서만 등장하는 아주 특별한 '부모님 소환권'이라고 보면 될 것 같다.
class TankLorry(Car):
    def __init__(self):
        super().__init__() # super()를 이용하여 부모클래스와 동일한 이름의 메서드의 어트리뷰트를  모두 상속받으면서도 수정권한을 가짐
        self.wheel_count = 10 # self.door_count는 그대로 유지한 채, self.wheel_count만 수정함.

    def start(self):
        super().start()
        print("ggggrrrrrrr..")