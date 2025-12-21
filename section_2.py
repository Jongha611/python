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