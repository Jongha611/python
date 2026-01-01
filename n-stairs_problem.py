# n칸의 계단을 오르는 경우의 수
# 한번에 1칸 또는 2칸의 계단만을 오를 수 있다.

"""
도착지점에서 2칸 남은 나와 1칸 남은 내가 있다.
도착지점에서 2칸 남은 지점에서 그 지점까지 2칸남은 나와 1칸남음 내가 있고, 도착지점에서 1칸 남은 지점에서 그 지점까지 2칸남은 나와 1칸 남은 내가 있다.

n = 1 -> f(1) = f(0) + f(-1) != 1 따라서, 이 부분은 초기 값으로 정해놓아야 한다.
n = 2 -> f(2) = f(1) + f(0) != 2 따라서, 이 부분은 초기 값으로 정해 놓아야 한다.
n = k -> f(k) = f(k-1) + f(k-2) = ? (when k:int > 2)
"""

def case_count(k):
    if k == 1:
        return 1
    elif k == 2:
        return 2
    else:
        total_count = case_count(k-1) + case_count(k-2)
        return total_count
print(case_count(3))