score_dict = {
    "student": ["Tom", "Lisa", "Sarah"],
    "score": [80, 90, 95]
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
    