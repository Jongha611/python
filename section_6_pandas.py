import pandas as pd

data = pd.read_csv("sample.csv")

# DataFrame : General 2D labeled, size-mutable tabular structure with potentially heterogeneously-typed column
print(type(data))
print(data.to_dict())

# Series : 1D labeled homogeneously-typed array
print(type(data['1']))
print(data['1'].to_list())

# # sum / max
# print(sum(data['population'].to_list()))
# print(data['population'].max())

# differct way to access to the column
# print(data.population)

# row data
# print(data[data.country == "USA"])
# print(data[data.population == data.population.max()])

# from scratch
grade = {
    "students": ["A", "B", "C"],
    "scores": [90, 80, 85]
}
data =pd.DataFrame(grade)
print(data)
data.to_csv("grade.csv")