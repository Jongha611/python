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

for i in range(2, int(ins_num**(1/2))):
    checker = ins_num % i
    if checker == 0:
        answer = "it's not"
        print(answer)
        break
    else:
        checklist.append(checker)
    
print(checklist)

if len(checklist) == (ins_num - 2):
    print("it's it")