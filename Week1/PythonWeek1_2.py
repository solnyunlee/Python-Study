# 2. 책 정보 출력 프로그램

book_info = {
    "HarryPotter1" : [[1997], [6], [26]],
    "TheLordOfTheRings" : [[1954], [7], [29]],
    "engineering_mathematics1" : [[2018], [2], [28]]
}

def info_choice():
    # 정보 선택창 출력
    print("------------------------------------")
    print("원하시는 정보를 선택해주세요.")
    print("1. 년")
    print("2. 월")
    print("3. 일")
    print("4. 종료")
    print("------------------------------------")

while True:
    # 책 제목 입력
    book_name = input("원하시는 책을 입력하세요.\n> ")

    # 책 제목이 딕셔너리 키에 존재하는 경우
    if book_name in book_info:
        # info_choice 함수를 이용하여 정보 선택창 출력
        info_choice()
        # 1~4 사이의 숫자 입력
        number = int(input())

        # 1을 입력한 경우 - 해당 책의 출판년도 출력
        if number == 1:
            print("{}년 입니다.".format(book_info[book_name][0][0]))
        # 2를 입력한 경우 - 해당 책의 출판 월 출력
        elif number == 2:
            print("{}월 입니다.".format(book_info[book_name][1][0]))
        # 3을 입력한 경우 - 해당 책의 출판 일 출력
        elif number == 3:
            print("{}일 입니다.".format(book_info[book_name][2][0]))
        # 4를 입력한 경우 - 프로그램 종료
        elif number == 4:
            print("프로그램이 종료되었습니다.")
            break

    # 책 제목이 딕셔너리 키에 존재하지 않는 경우 - 책 제목 재입력
    else :
        print("제목을 다시 입력해주세요.")