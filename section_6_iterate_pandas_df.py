score_dict = {
    "student": ["Tom", "Lisa", "Sarah", "Jongha"],
    "score": [80, 90, 95, 99]
}


# 판다스 없이 Iterating Thru
[print(col) for (col, _) in score_dict.items()]


# 판다스
import pandas as pd

score_df = pd.DataFrame(score_dict)
print(score_df)

for (key, value) in score_df.items():
    print(key)
    print(value)
    
    
# loop through raws
for (i, row) in score_df.iterrows():
    print(f"{row.student}: {row.score}")
    

# 판다스스럽게 리팩토링하기
print(score_df)

# 판다스의 subscript #1
ref_score_df = score_df["score"][2]
print(ref_score_df)

# 판다스의 subscript #2: .iloc() integer location
print("판다스의 subscript #2: .iloc() integer location")
iloc_score_df = score_df.iloc[2, 1]
print(iloc_score_df)

# 판다스의 subscript #3: .loc() labeled location
print("판다스의 subscript #3: .loc() labeled location")
lloc_score_df = score_df.loc[2, "score"]
print(lloc_score_df)


# 판다스의 Boolean Subscripting
bool_score_df = score_df["score"] > 89 # True와 False로 이루어진 DF를 반환
print(bool_score_df)

bool_score_df2 = score_df[score_df["score"] > 89] # 위의 불리언 DF를 다시 재 subscript하면 True만을 선택한다.
print(bool_score_df2)
# 파이썬이라는 언어에서는 True는 선택 False는 버림 을 의미한다고 한다. 