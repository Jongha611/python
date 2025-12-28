# print

print('home', "user", "network", sep="/")

# input
'''
age = input("what is your age?")

print(f"my name is {age}")
print(f"my name is" + " " + age)

frame = "my name is"

final = " ".join(age)
print(final)
'''
example = "가나 다라마 바사아자 차카타 파 하" # 튜플은 되는데 리스트는 안 된다.
final2 = example.split(" ")
print(final2)

# Floats(Decimal Point)
score = float(59)
print(score)

score = int(59.6)
print(score)

# 문자 연산자
print(3 ** 3)
print(5 // 3)

# modulo
print(5 % 3)

# json

profile = {
    "name": "김종하",
    "age": 36,
    "sex": "male",
    "hobby": "develop"
}

print(profile["age"])


# 반드시 리턴해야만 함수가 영향력을 미치는 것은 아니다. 자세한 내용은 md 가변 및 불변데이터 표 참조.
def paint_door(house):
    house['door_color'] = 'Red'  # 이 순간 메모리의 해당 주소 데이터가 바뀜 (즉시 반영)
    # return 없음
    return None

my_house = {'door_color': 'White'}
paint_door(my_house)

print(my_house)  # {'door_color': 'Red'}


# isisntance: isinstance(value, type)
a = 37.3

if not isinstance(a, int):
    result = int(a)
else:
    result = a
print(result)


# try-except의 쓰임. md문서 참조.
# input함수는 반드시 문자열로 리턴한다.
'''
import re

b = input("insert any number: ")

def preprocess(thing):
    try:
        path1 = float(thing)
        result = int(path1)        
    except Exception:
        clean_thing = re.sub('"', '', thing)
        lange = len(clean_thing)
        # print(f"{clean_thing}의 길이는 {howlongthing}")
        result = clean_thing + str(lange)
        print(f"{thing} is unknown")
    return result

e = preprocess(b)
print(e)
'''


# random module
import random

test_random = random.randint(1, 100)
print(test_random)

import random_module

module_test = random_module.MY_LOCATION
print(module_test)



# random.random과 random.randint는 각각의 강점을 가진다.
# numpy와 pytorch의 random.rand는 훨씬 강력한 도구이다.
random_int = random.random()
print(int(random_int*10))

my_random_int = random.randint(0, 9)
print(my_random_int)


# 초미니 프로젝트: 동전 앞 뒤 맞추기 게임
import random
user_response = input("동전을 던지시겠습니까? (y 또는 n 입력): ").strip().lower()

if user_response == "y" or "yes":
    coin_result = random.randint(0, 1)
    if coin_result == 1:
        print("앞면!")
    else:
        print("뒷면!")
else:
    print("동전을 왜 던져? 돈가지고 장난치는거 아니지..")
    
