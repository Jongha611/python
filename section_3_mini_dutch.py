# goint dutch
num_of_ppl = int(input("더치페이 인원은 몇명입니까? "))
# ⚠️ 개선 포인트:
# - strip()을 붙이지 않으면 " 3 " 같은 입력에서 ValueError 발생 가능
# - num_of_ppl == 0 인 경우 ZeroDivisionError 발생 가능 (방어 로직 없음)

food_price = []

def input_parser(s: str):
        # if s.startswith('"') and s.endswith('"'): # 좋은 기능이지만 지금은 부적합하다. '"'를 문자열 접두사or접미사로 인식하지 않는다. 굳이따지면 필요없다. input()은 항상 문자열을 반환하므로
        
        # ⚠️ isdigit()의 한계:
        # - 음수(-100) ❌
        # - 실수(3.14) ❌
        # - 공백 포함(" 300 ") ❌
        # - 쉼표("1,000") ❌
        # 현재 정책상 "양의 정수 문자열"만 허용하는 구조
        if s.isdigit():
            return int(s)
        else:
            # 숫자가 아니면 그대로 문자열 반환
            # 이 값은 while 루프에서 종료 신호로 사용됨
            return s

while True:
    inserted_food_price = input(
        "음식의 가격을 입력해주세요(다 입력했을 경우 아무 문자열이나 입력해서 종료): "
    )
    # print(inserted_food_price.startswith('"') and inserted_food_price.endswith('"')) 
    # ⚠️ startswith / endswith 디버깅은 좋았음
    # 다만 현재 정책에서는 따옴표 여부와 무관하므로 제거해도 무방
    
    result = input_parser(inserted_food_price)
    # ⚠️ result는 여기서 "int 또는 str" 두 가지 타입을 가질 수 있음
             
    if isinstance(result, int):
        food_price.append(result)
    else:
        # 숫자가 아닌 입력이 들어오면 입력 종료
        break

# ⚠️ 디버깅 출력
# - 학습 단계에서는 좋음
# - 실전 코드에서는 제거 대상
print(isinstance(result, int))
print(type(result))
print(result)
print(food_price)

def going_dutch(num_of_ppl, food_price):
    food_price_sum = 0
    
    # ⚠️ Python에서는 sum(food_price)로 한 줄에 가능
    # 현재 for-loop는 로직 이해 연습용으로는 적절
    for i in range(0, len(food_price)):
        food_price_sum += food_price[i]
    
    # ⚠️ num_of_ppl == 0 이면 ZeroDivisionError
    pay_per_person = food_price_sum / num_of_ppl
    return pay_per_person

result = going_dutch(
    food_price=food_price,
    num_of_ppl=num_of_ppl
)
# ⚠️ result 변수명 재사용:
# - 위에서는 input 파싱 결과
# - 여기서는 계산 결과
# 실전에서는 의미 충돌을 피하기 위해 다른 이름 권장

print(result)
