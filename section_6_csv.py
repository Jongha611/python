# csv: comma-seperated-value

# using file management
with open("sample.csv", "r") as csv_file:
    csv = csv_file.read()
print(csv)


# using csv package
import csv

with open("sample.csv", "r") as csv_file2:
    csv2 = csv.reader(csv_file2)
    print(csv2)
    for row in csv2:
        print(row[2]) # 줄마다 길이가 달라서 없는 부분에 대해 pandas는 nan으로 보여주지만 csv package는 에러를 띄운다.

        
# using pandas
import pandas as pd

csv3 = pd.read_csv("sample.csv")
print(csv3)

print(csv3["1"])