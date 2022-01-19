# 1. 구구단 출력문제

def print_initial():
    # 처음 실행화면 출력
    print("---------------------------------------------------------------")
    print("\"구구단을 외자, 구구단을 외자\" 프로그램을 실행합니다.")
    print("1. 홀수 구구단")
    print("2. 짝수 구구단")
    print("3. 종료")
    print("---------------------------------------------------------------")

def func_gugudan(n):
    # 출력하고자 할 단 출력
    print("{}단".format(n))
    # 1부터 9까지 곱하여 출력
    for i in range(1, 10):
        print("{} * {} = {}".format(n, i, i*n))

while True:
    # print_initial 함수를 이용하여 처음 실행화면 출력
    print_initial()
    # 숫자를 입력받아 해당하는 명령 실행
    number = input("숫자를 입력하세요: ")

    if number == "1":
        # 3단부터 9단까지 홀수단 출력
        for i in range(3, 10, 2):
            func_gugudan(i)

    elif number == "2":
        # 2단부터 8단까지 짝수단 출력
        for i in range(2, 9, 2):
            func_gugudan(i)

    elif number == "3":
        # 프로그램 종료
        print("프로그램을 종료합니다.")
        break
    
    else :
        # 잘못 입력한 경우
        print("잘못 입력하셨습니다. 1~3 번 숫자를 입력하세요")