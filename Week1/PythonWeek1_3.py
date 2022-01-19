# 3. 신규 아이디 추천

def solution(id):
    # 단계1 - 대문자를 소문자로 치환
    step1_id = id.lower()
    print(step1_id)
    # 단계2 - 특수문자 제거
    step2_id = remove_ch(step1_id)
    # 단계3 - 연속된 마침표를 하나의 마침표로 치환
    step3_id = replace_period(step2_id)
    # 단계4 - 처음과 끝의 마침표 제거
    step4_id = step3_id.strip(".")
    print(step4_id)
    # 단계5 - 문자열의 공백 확인
    step5_id = check_empty(step4_id)
    # 단계6 & 단계7 - 문자열 길이 확인
    step67_id = check_len(step5_id)
    new_id = step67_id
    return new_id

def remove_ch(id):
    special_ch = "~!@#$%^&*()=+[{]}:?,<>/"
    # id의 특수문자 제거
    for element in special_ch:
        if element in id:
            id = id.replace(element, "")
    print(id)
    return id

def replace_period(id):
    # id의 연속된 마침표 제거
    while ".." in id:
        id = id.replace("..", ".")
    print(id)
    return id

def check_empty(id):
    # id가 공백인 경우 a를 대입
    if id == "":
        id = "a"
    print(id)
    return id

def check_len(id):
    # id의 길이가 16이상인 경우
    if len(id) >= 16:
        # id의 15자만 유지
        id = id[:15]
        # id 끝에 마침표가 있다면 제거
        id = id.rstrip(".")
    # id의 길이가 2이하인 경우
    elif len(id) <= 2:
        # 길이가 3이 될 때까지 id의 마지막 문자를 끝에 붙임
        while len(id) < 3:
            id = id + id[len(id)-1]
    print(id)
    return id

# 아이디 입력
new_id = input("ID: ")
# solution 함수를 이용하여 추천 아이디 출력
answer = solution(new_id)
print("new_id: {}".format(answer))