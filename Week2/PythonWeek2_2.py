# 2. 하노이탑

# 하노이탑 재귀함수
def hanoi_tower(num, first, second, third):
    # 원판이 1개인 경우
    if num == 1:
        # 원반을 첫번째 장대에서 세번째 장대로 이동
        print(first, third)
    else:
        # 원반 (num-1)개를 첫번째 장대에서 두번째 장대로 이동
        hanoi_tower(num-1, first, third, second)
        # 가장 큰 원반을 첫번째 장대에서 세번째 장대로 이동
        print(first, third)
        # 원반 (num-1)개를 두번째 장대에서 세번째 장대로 이동
        hanoi_tower(num-1, second, first, third)

# 원반 개수 입력
k = int(input())
# 원반 이동 횟수 출력
print(2**k - 1)
# 수행 과정 출력
hanoi_tower(k, 1, 2, 3)