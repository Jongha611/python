# Assignment Operator
# Assignment with an = on lists does not make a copy. 
# Instead, assignment makes the two variables point to the one list in memory.

# colors는 리스트 객체를 포인트 했음. b = colors 라는 별개의 카피 객체를 가지고 있는 것이 아니다.
# b와 colors 라는 변수 둘 다 원본 list object의 address를 포인팅 하고 있다.
colors = ["red", "blue", "yellow"]
b = colors

b.append("white")
print(b, colors)


# Shallow Copy
# A Shallow copy constructs a new compound object and then (to the extent possible) inserts references...
# ...into it to the object found in the original.
a = [[1, 2], [2, 4]]
b = a[:] # shallow copy

b[0].append([3, 6])

print(a)
print(b)

b[0].append(7)

print(a)
print(b)


# Deep Copy
# A deep copy construts a new compound object and then, recursively, inserts copy...
# ...into it of the object found in the original.
import copy

a = [[1, 2], [2, 4]]
b = copy.deepcopy(a) # deep copy

b[0].append(3)

print(a)
print(b)

print(id(a) == id(b))


# scope
# local scope / global scope / enclosed scope / enclosing scope
# namespace

my_score = 50 # global scope

def inside_value_function():
    # global my_score
    my_score = 80
    print(f"my inside score is {my_score}")
    return

inside_value_function()
print(f"my_outside_scope is {my_score}")


# what about if condition 
did_extra_work = True
if did_extra_work:
    my_score = 90
print(my_score)


# nonlocal
def a():
    x = 10
    def b():
        # nonlocal x
        x = 20
        return
    b()
    print(x)
    return
a()


# How Python search the variable?
# (LEGB rule)
# 1. local: 해당 로컬
# 2. enclosing: 가장 가까운
# 3. global: 글로벌
# 4. built-in: 파이썬 내장

# builtin namespace
print(dir(__builtins__))


# Example
country = ["south korea"]

def inside_list_function():
    country.append("usa") # country 를 local(함수 내부 namespace)에서 정의하지 않았으므로 찾을 수 없다. 따라서 함수 외부 enclosing의 country를 찾아서 수행.
    # country = ["usa"]
    
inside_list_function()
print(country)


# globals keyword
print(globals())


# Global Constant?
# 1. '도메인' 혹은 '기본 주소'임을 명시합니다.
BASE_URL = "http://yelp.com"

# 2. 엔드포인트는 함수 내부에서 정의하거나 별도의 상수로 관리합니다.
def print_us_restaurant_url():
    # 실제 엔드포인트 경로: /biz/arya-steakhouse-palo-alto
    endpoint = "/biz/arya-steakhouse-palo-alto"
    print(f"{BASE_URL}{endpoint}")

def print_korean_restaurant_url():
    endpoint = "/biz/tobang-santa-clara-2"
    print(f"{BASE_URL}{endpoint}")
    
print_us_restaurant_url()
print_korean_restaurant_url()


# # How to debug?
# 1. Explain the problem
# 2. Produce the bug again to see what went wrong
# 3. Evaluate the line by line
# 4. Check the underline portion
# 5. Use print()
# 6. Fix the error


# Frequent error from novice
import math

number = [34 ,25, 56, 76, 31, 26]
minimum = math.inf

for n in number:
    if n < minimum:
        minimum = n
print(minimum)