# find a prime number
ins = ""

while True:
    if ins.isdigit():
        ins_num = int(ins)
        break
    elif ins.lower().strip() == "exit":
        print("bye~")
        break
    else:
        ins = input("is this prime number? ")
print(ins_num)

checklist = []

# for i in range(2, ins_num):
#     checker = ins_num % i
#     if checker == 0:
#         answer = "it's not"
#         print(answer)
#         break
#     else:
#         checklist.append(checker)
    
# print(checklist)

# if len(checklist) == (ins_num - 2):
#     print("it's it")

# for i in range(2, int(ins_num**(1/2))+1):
#     checker = int(ins_num) % i
#     if checker == 0:
#         answer = "it's not"
#         print(answer)
#         break
#     else:
#         checklist.append(checker)
    
# print(checklist)

# if len(checklist) == (int(ins_num**(1/2))-1):
#     print("it's it")
    

# num = int(input("insert the number: "))
# if num > 1:
#     is_divisible = False
#     length = int(num**(1/2))+1
#     for i in range(2, length):
#         if num % i == 0:
#             is_divisible = True
#             print(f"{num} is can be cleared diveded by {i}")
#             break
#     if is_divisible:
#         print(f"{num} is not prime number")
#     else:
#         print(f"{num} is a prime number")
# else:
#     print("it's not")
    
    
import math

num = int(input("insert the number: "))

if num > 1:
    # 2부터 제곱근까지만 확인
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            print(f"{num} is not prime number (divided by {i})")
            break
    else:
        # break가 걸리지 않고 루프가 끝까지 돌았을 때만 실행됨
        print(f"{num} is a prime number")
else:
    print(f"{num} is not prime number")