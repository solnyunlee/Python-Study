# 2. 구명보트

def solution(people, limit):
    # 사람들의 몸무게 배열을 오름차순으로 정렬
    people.sort()
    # 필요한 구명보트의 수
    boat = 0
    # 배열의 첫번째 인덱스 (몸무게 최솟값)
    min = 0
    # 배열의 마지막 인덱스 (몸무게 최댓값)
    max = len(people) - 1

    while min <= max:
        # 보트 수 증가
        boat += 1
        # 몸무게 최댓값과 최솟값의 합이 무게 제한보다 작거나 같은 경우 - 2명 탑승 가능
        if people[min] + people[max] <= limit:
            # 몸무게 최솟값 구명보트 탑승 완료
            min += 1
        # 몸무게 최댓값 구명보트 탑승 완료
        max -= 1
    return boat

# 인원 수와 구명 보트의 무게 제한 입력
n = int(input("인원을 입력하세요.\n>> "))
limit = int(input("구명보트의 무게 제한을 입력하세요.(40 ~ 240)\n>> "))
people = []
count = 0

# 인원 수만큼 몸무게를 입력
print("{}명의 몸무게를 입력하세요.\n>>".format(n))
while count < n:
    weight = int(input())
    # 몸무게가 구명보트의 무게 제한을 초과하지 않는 경우
    if weight <= limit:
        # 배열에 몸무게 추가
        people.append(weight)
        count += 1

print(solution(people, limit))