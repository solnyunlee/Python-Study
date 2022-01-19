# 3. 최소 합계와 최대 합계

import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    # 리스트 요소를 모두 더한 뒤 최댓값을 뺀다.
    arr_min = sum(arr) - max(arr)
    # 리스트 요소를 모두 더한 뒤 최솟값을 뺀다.
    arr_max = sum(arr) - min(arr)
    # 최솟값과 최댓값 출력
    print(arr_min, arr_max)

# 5개의 정수를 리스트에 입력
arr = list(map(int, input().rstrip().split()))
# miniMaxSum 함수로 최솟값과 최댓값 출력
miniMaxSum(arr)