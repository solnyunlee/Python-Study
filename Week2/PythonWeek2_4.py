# 4. Class 계산기

import math

class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    # 덧셈
    def add(self):
        return self.a + self.b
    # 뺄셈
    def sub(self):
        return self.a - self.b
    # 곱셈
    def mul(self):
        return self.a * self.b
    # 나눗셈 (0인 경우 제외)
    def div(self):
        if self.b == 0:
            print("0으로 나눌 수 없습니다.")
        else:
            return self.a / self.b

# calculator class 상속
class improved_calculator(calculator):
    # 제곱
    def pow(self):
        return math.pow(self.a, self.b)
    # 최대 공약수
    def gcd(self):
        return math.gcd(self.a, self.b)

def initial_info():
    print("아래에 사용을 원하시는 사칙연산을 선택해주세요!")
    print("1. 더하기")
    print("2. 빼기")
    print("3. 곱하기")
    print("4. 나누기")
    print("5. 제곱")
    print("6. 최대 공약수")
    print("7. 종료")

def main():
    while True:
        # 초기화면 출력
        initial_info()
        # 명령 입력
        index = int(input(">> "))
        # 입력받은 명령이 7인 경우 - 프로그램 종료
        if index == 7:
            print("계산기 프로그램을 종료합니다.")
            break
        else:
            # 두 수 입력
            a, b = map(int, input("두 숫자를 입력해주세요: ").split())
            result = improved_calculator(a, b)
            # 입력받은 명령이 1인 경우 - 덧셈 출력
            if index == 1:
                print(result.add())
            # 입력받은 명령이 2인 경우 - 뺄셈 출력
            elif index == 2:
                print(result.sub())
            # 입력받은 명령이 3인 경우 - 곱셈 출력
            elif index == 3:
                print(result.mul())
            # 입력받은 명령이 4인 경우 - 나눗셈 출력
            elif index == 4:
                print(result.div())
            # 입력받은 명령이 5인 경우 - 제곱 출력
            elif index == 5:
                print(result.pow())
            # 입력받은 명령이 1인 경우 - 최대공약수 출력
            elif index == 6:
                print(result.gcd())
            print()
            
# 실행
main()


