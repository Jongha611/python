# country => parameter
# "USA" => argument


# Position Argument
def travel_to_country(name: str, country: str):
    print(f"안녕하세요. {name}님!")
    print(f"{country}까지 좋은 여행 되시기 바랍니다.")
    
travel_to_country("미국", "종하")


# Keyword Argument
travel_to_country(
    country = "일본",
    name = "종하"
)