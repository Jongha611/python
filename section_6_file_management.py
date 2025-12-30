# file management

# read
file = open("README.md", "r", encoding = "utf-8" )
result = file.read()
file.close()
print(result)

# garbage collector
with open("README.md", "r", encoding="utf-8") as f:
    result2 = f.read()
print(result2)

# write
with open("WRITEME.md", "w", encoding="utf-8") as f2:
    result3 = f2.write("modified!")
print(result3)