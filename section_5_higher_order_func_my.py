def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2, is_floor=True):
    if is_floor:
        return num1 // num2
    else:
        return num1 / num2

calculation_tools = {
    "+": add,
    "*": multiply,
    "-": subtract,
    "/": divide
}



# functionize
def inputer(func):
    def wrapper():
        inserted = input("연산기호를 입력해주세요: ")
        selected_func = calculation_tools.get(inserted)
        if selected_func == None:
            result = print("지원하지 않는 연산자입니다.")
            pass
        else:
            a = int(input("a 입력: "))
            b = int(input("b 입력: "))
            result = func(a, b, inserted)
            return result
        
    return wrapper

@inputer
def cal_router(a, b, inserted):
    selected_func = calculation_tools.get(inserted)
    result = selected_func(a, b)
    return result

print(cal_router())
    

# def first(func):
#     # print("first의 영역") #
#     def first_inside(): # wrapper: 포장지 데코레이터를 받는 메인 함수를 감싼다.
#         print("first_inside의 영역")
#         func()
#         return
#     return first_inside

# @first
# def second():
#     print("second의 영역")
#     return

# # second(데코레이션을 받은 그리고 변형될 메인함수는) = first(나중에 붙인 데코레이션에)(second(그 함수를 대입한 것이)) 할당되는것이다.
# # 데코레이터는 인터프리터 입장에서는 함수를 데코레이터를 만나는 순간이 바로 해당 함수를 재정의하기 위한 실행시점이다.

# second()