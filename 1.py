# 가변인자 공부

def grade(**kwargs):
    for k, v in kwargs.items():
        print(f"무언지 모르는 미래의 목록은 다음과 같다. {k}: {v} ")
        
dictionary = {"a": 1, "b": 2, "c": 3, "d": 4}

grade(**dictionary)