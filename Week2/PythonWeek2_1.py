# 1.업샘플링

# 정사각형의 가로세로 길이 n과 배수 k 입력
n, k = map(int, input("N, K: ").split())
# 픽셀 정보를 입력받을 리스트 선언
pixel_info = []
for i in range(n):
    # 픽셀 정보를 입력받아 리스트에 추가
    pixel_info.append(list(map(int, input().split())))

# k배 늘어난 픽셀 정보 출력
print("After Up sampling")
for i in range(n):
    for r in range(k):
        for j in range(n):
          for c in range(k):
                print(pixel_info[i][j], end = " ")
        print()
