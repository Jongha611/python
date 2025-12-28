# 문자열 뒤집기: 인터뷰 예제
# Revers String

value = "Hello, World"

list_value = list(value)

print(list_value)
print(len(list_value))

length = len(list_value)
reverse_string = []

for n in range(0, length):
    reverse_order = length - 1 - n
    reverse_string.append(list_value[reverse_order])
print(reverse_string)

result = "".join(reverse_string)

print(result)

# .reverse 사용, reversed 펑션 사용, while 사용, :: 사용 등등 방식은 많음


# while, pop 사용
reverse_string2 = []

while True:
    reverse_string2 += list_value.pop()
    if len(reverse_string2) > 11:    
        break
    
print("".join(reverse_string2))