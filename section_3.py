# List Struture
# when to use?
# - Grouping
# - Keep the order
from operator import add


countries = ["South Korea", "USA", "Japan", "China"]

countries[2] = "Vietnam"

print(countries)

# list + list
element = "c"

alphabets = ["a", "b", element, "d"]

print(alphabets)

alphabets_extra = ["e", "f"]

added_alphabets = alphabets + alphabets_extra

print(added_alphabets)

print(added_alphabets[-1])

print(len(added_alphabets)-1)


# in_place 연산
added_alphabets.append("g") # 추가, 그러나 + 와는 다른 인플레이스 연산

print(added_alphabets)

added_alphabets.insert(1, "start") # 삽입, 인덱스는 첫 번째 문자열의 앞 공백 부터 시작된다.

print(added_alphabets)

added_alphabets.pop(1) # 제거

print(added_alphabets)


# Nested list
alphabets = [["a", "b", "c"], ["d", "e"]]


# 반복문 for
numbers = (1, 2, 5, 3, 8, 4)
sum = 0

for i in numbers:
    sum += i
print(sum)

average = sum/len(numbers)
print(average)

max_num = 0
for number in numbers:
    if number > max_num:
        max_num = number
print(max_num)


# odd number?
odd = []
for i in range(0, 15):
    if i%2 == 0:
        odd.append(i)
print(odd)

# FizzBuzz 인터뷰 문제
result  = []
n = int(input("배열의 길이를 정해주세요: "))
# 파이썬에서 range(1, n)은 n을 포함하지 않는다 n-1의 길이만큼을 처음 숫자를 포함하여 계산. (이 발상이 슬라이스와 완벽 호환되기 때문)
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0: # 또는 if i % 15 == 0:
        result.append("FizzBuzz")
    elif i % 3 == 0:
        result.append("Fizz")
    elif i % 5 == 0:
        result.append("Buzz")
    else:
        result.append(str(i))
print(result)
# if-elif와 수학적 공배수 관계를 고려하여 개선된 코드를 작성해볼것.


