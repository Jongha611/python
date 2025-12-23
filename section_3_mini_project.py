# 초미니 프로젝트: 강력한 패스워드를 생성해주는 프로그램을 만들어보자.
alphabets = "abcdefghijklmnopqrstuvwxyz"

lower_alphabets = []
for char in alphabets:
    lower_alphabets.append(char)
print(lower_alphabets)

attached_upper_alphabets = alphabets.upper()
# upper_alphabets = ", ".join(attached_upper_alphabets)
# print(upper_alphabets)

upper_alphabets= []
for char in attached_upper_alphabets:
    upper_alphabets.append(char)
print(upper_alphabets)

numbers = []
for number in range(0, 10):
    numbers.append(str(number))
print(numbers)

special_chars_init = "!@#$%^&*()"
special_char = []

for char in special_chars_init:
    special_char.append(char)
print(special_char)

char_list = [upper_alphabets, lower_alphabets, numbers, special_char]

import random

random_upper = random.choices(upper_alphabets, k=4)
random_lower = random.choices(lower_alphabets, k=4)
random_number = random.choices(numbers, k=4)
random_char = random.choices(special_char, k=4)

linked_password = random_lower + random_upper + random_number + random_char

print(linked_password)

random.shuffle(linked_password)

print(linked_password)

password = ""

for i in range(0, len(linked_password)):
    password += linked_password[i]
print(password)