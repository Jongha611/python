섹션 3 강의노트: 

https://drive.google.com/file/d/1LDI4s78cmc3oong_D-NdK3rXmOJ1gyMe/view?usp=sharing

1. 자료구조와 인플레이스 연산

https://docs.python.org/3/tutorial/datastructures.html

| 목적 | 방법 |
| --- | --- |
| 새 리스트 필요 | `a = b + [x]` |
| 기존 리스트 수정 | `b.append(x)` |

이 둘을 **절대 섞지 않는다**.

---

### 왜 `append()`가 값을 반환하면 안 되느냐 (핵심)

만약 이게 허용되면:

```python
a = b.append(x)

```

코드만 보고는 **절대 알 수 없다**:

- `b`가 바뀌었는지
- 안 바뀌었는지
- `a`와 `b`가 같은 객체인지

Python은 이 모호함을 **언어 차원에서 금지**했다.

그래서, `b.append(x) # 문장(statement)` 으로만 쓰게 만든다.

즉, 마지막으로, 한 문장으로 정리

**Python은 “리스트를 편집하는 행위”와 “새 리스트를 만드는 행위”를 같은 메서드 이름 아래 두지 않기로 선택했다.**

그래서 네가 말한 설계는 **가능하지만**, Python이 **의도적으로 버린 설계**다.

이 개념과 연관지어 지금 막힌 지점은 **mutable(뮤터블)** 하나다.

이거 하나만 정확히 잡으면 앞의 모든 말이 **한 번에 연결**된다.

아주 단순하게 간다.

### mutable이 무슨 뜻이냐?

- mutable = 같은 객체를 가리킨 채로, 내용만 바뀔 수 있다
- **immutable = 내용이 바뀌면 아예 새 객체가 생김**

1. 파이썬 빌트인 펑션

https://docs.python.org/3/library/functions.html

1. pop은 삭제가 아니라 꺼내기 메서드다.
- 인플레이스 연산으로 삭제를 하지만, 그 값은 반환되어 객체 할당 가능하다.

1. json에서 자주 보이던 데이터 형태는 nested data structure이다.
- list 안에 dictionary, 그 안에 list 등등

1. 딕셔너리 접근 메서드
- `dictionary_name.items()`
- `dictionary_name.keys()`
- `dictionary_name.values()`
- 리스트처럼 `dictionary_name[”key_name”]` 으로 조회 가능