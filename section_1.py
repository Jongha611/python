# enumerate() 함수는 리스트의 인덱스와 값을 함께 반환한다.
# 튜플 형태로 반환된다.
c = ['g','r','h','e','d','f','v','v','g']

for a, b in enumerate(c):
    print(a, b)

# 재귀함수
def factorial(n):
    return 1 if n == 1 else n * factorial(n-1)

result = factorial(5)
print(result)



# **kwargs는 인자를 딕셔너리 형태로 받는다.
# 즉, 인자로 얼마나 많은 딕셔너리가 들어올지 모를 때, 쓰면 좋다.
config = {"host": "localhost", "port": 8000, "debug": True}

def print_config(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")
        
result = print_config
result(**config)

# 메서드는 클래스에 종속된 함수를 의미한다.
class CalculationFactory:
    def __init__(self, b):
        self.b = b
    def add(self, a):
        c = a + self.b
        return c
    
calculator = CalculationFactory(5)

calculator.add(2)

print(c)

