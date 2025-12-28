# Custom Class
# naming convention
# camelCase: object name
# snake case: anything else

from turtle import speed


class Car:
    def __init__(self, color, engine_type): # constructor
        self.color = color
        self.engine_type = engine_type
        self.speed = 0
        self.is_start = False
        
    def start_engine(self): # 클래스 내에서 함수를 정의 -> 메서드 <=> 메서드의 정의: 클래스 함수
        self.speed = 0
        self.is_start = True
        
    def speed_up(self, speed):
        self.speed += speed
        
    def speed_down(self, speed):
        self.speed -= speed
        
    # pass # 땡땡이 뒤에 아무것도 안넣으면 에러남. 그래서 빈공간이라는 의미의 pass 넣을 수 있음.

tesla = Car( # self 파라미터 자리에 알규먼트가 들어가야 하나? 그렇지 않다. 자동으로 들어간다.
    color = "green",
    engine_type = "electric"
)
# tesla.color = "red"
# tesla.engine_type = "electric"

print(tesla.color)

# How to list all the attributes?
print(vars(tesla)) # vars: object에 어떤 attributes가 있는지 확인하는 펑션

# construtor: class 에 리절브된 펑션
# def __init__(self):
# when is called?

tesla.start_engine()
print(vars(tesla)) # vars: object에 어떤 attributes가 있는지 확인하는 펑션

tesla.speed_up(30)
print(vars(tesla)) # vars: object에 어떤 attributes가 있는지 확인하는 펑션