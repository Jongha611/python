# Arguments with Default Values
def write_str_to_file(file_name, content, mode="w"):
    with open(file_name, encoding="utf-8", mode=mode) as f:
        f.write(content)
        
write_str_to_file(
    file_name="default_values.md",
    content="\nhello world",
    mode="a" # append를 의미  # mode = mode = "W"로 함수설계에서 정의했으므로  
)


# # Unlimited Positional Arguments
# def unlimited_func(*args):
#     print(args)
# unlimited_func(1, 2, 3)

# def sum_all(*args): # *args
#     total = 0
#     for n in args:
#         total += n
#     return total
# print(sum_all(1, 2, 3, 4, 5, 6))


# **kwargs: Keyworded arguments
def calc(**kwargs):
    print(kwargs)
    
calc(n1=1, n2=3, func="add")

def calc(**kwargs):
    for k, v in kwargs.items():
        print(k)
        print(v)
        
    if kwargs["func"] == "add":
        return kwargs["n1"] + kwargs["n2"]
    
print(calc(n1=1, n2=3, func="add"))