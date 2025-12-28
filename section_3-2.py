# country => parameter
# "USA" => argument


# Position Argument: 자리에 맞는 인자를 입력해야 한다.
def travel_to_country(name: str, country: str):
    print(f"안녕하세요. {name}님!")
    print(f"{country}까지 좋은 여행 되시기 바랍니다.")
    
travel_to_country("미국", "종하")


# Keyword Argument: 키워드인자, 인자 자체를 정의해서 입력.
travel_to_country(
    country = "일본",
    name = "종하"
)
# Positional Argument는 자리가 고정되는 것이 매우 까다롭기 때문에 대부분의 Developer들은 Keyword Argument를 사용한다.


# Dictionary

dic = {
    "country": "south korea",
    "city": "Seoul",
    "gender": "male",
    "age": "35"
}

for key, value in dic.items():
    print(f"{key}: {value}")
    
for key in dic:
    print(f"{key}: {dic[key]}")
    
print(dic["country"])
    
print(dic.keys(), dic.values())