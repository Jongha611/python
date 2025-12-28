https://drive.google.com/file/d/15rZcyF9nC2Lcf6F5BAgJQDYpbkacwfQF/view?usp=sharing

1. Assignment vs Shallow copy vs Deep copy
- Assignment는  이름만 다른 포인터 두 개가 같은 오브젝트(주소가 같음)를 가리키도록 할당
- Shallow copy는 주소가 다른 새로운 컴파운드를 만들긴 하지만 내부 오브젝트들은 원본과 같으며(주소가 같음) 포인터들도 같은 주소를 가리키도록 할당
- Deep copy는 주소가 다른 완전히 새로운 컴파운드를 만들며 내부도 역시 원본으로부터 복사된 새로운 주소를 가지는 객체가 된다. 포인터들은 Deepcopy 된 컴파운드의 전체 원본과 다른 주소로 카리킨다.

1. Assignment (할당)

- **핵심:** **Alias (별칭) 생성.**
- **상태:** 새로운 객체도, 새로운 주소값도 생성되지 않음.
- **메모리:** 하나의 주소값을 두 변수(포인터)가 공유함.
- **위험:** 어느 한쪽 이름을 통해 데이

2. Shallow Copy (얕은 복사)

- **핵심:** **껍데기만 복제.**
- **상태:** 최상위 컴파운드 객체는 새로운 주소를 가짐.
- **내부:** 하지만 내부 요소들은 **원본 요소들의 주소값(포인터)을 그대로 복사**해옴.
- **참사 포인트:** 리스트 안에 리스트가 있는 경우, 내부 리스트의 주소가 같기 때문에 내부 요소를 수정하면

3. Deep Copy (깊은 복사)

- **핵심:** **재귀적 완전 복제.**
- **상태:** 최상위뿐만 아니라 내부에 중첩된 모든 컴파운드 객체들을 새로 생성하여 새로운 주소를 부여함.
- **결과:** 원본과 복사본 사이에 공유하는 메모리 주소가 단 하나도 없음.
- **비용:** 가장 안전하지만, 데이터가 클수록 복사 속도가 느리고 메모리 점유율이 높음.

1. LEGB rule

```python
# How Python search the variable?
# (LEGB rule)
# 1. local: 해당 로컬
# 2. enclosing: 가장 가까운
# 3. global: 글로벌
# 4. built-in: 파이썬 내장
```

1. ENDPOINT와 BASE_URL의 차이

```python
# Global Constant?
# 1. '도메인' 혹은 '기본 주소'임을 명시합니다.
BASE_URL = "http://yelp.com"

# 2. 엔드포인트는 함수 내부에서 정의하거나 별도의 상수로 관리합니다.
def print_us_restaurant_url():
    # 실제 엔드포인트 경로: /biz/arya-steakhouse-palo-alto
    endpoint = "/biz/arya-steakhouse-palo-alto"
    print(f"{BASE_URL}{endpoint}")

def print_korean_restaurant_url():
    endpoint = "/biz/tobang-santa-clara-2"
    print(f"{BASE_URL}{endpoint}")
```

1. 파이썬 디버깅

```python
# # How to debug?
# 1. Explain the problem
# 2. Produce the bug again to see what went wrong
# 3. Evaluate the line by line
# 4. Check the underline portion
# 5. Use print()
# 6. Fix the error
```