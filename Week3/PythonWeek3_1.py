# 1. 스택 활용문제

import sys

class Stack:
    # 리스트를 이용하여 스택 생성
    def __init__(self):
        self.list = []
    # push
    def push(self, data):
        self.list.append(data)
    # pop
    def pop(self):
        return -1 if len(self.list) == 0 else self.list.pop()
    # size 
    def size(self):
        return len(self.list)
    # empty (정수가 비어있으면 1, 아니면 0 출력)
    def empty(self):
        return 1 if len(self.list) == 0 else 0
    # top 
    def top(self):
        return self.list[-1] if len(self.list) > 0 else -1

# 명령의 수 입력
n = int(input("명령의 수: "))
stack = Stack()
# 명령의 수만큼 for문 실행
for _ in range(n):
    # 명령 입력
    cmd = sys.stdin.readline().split()
    
    # 명령이 "push"인 경우 - 스택에 정수를 넣어준다.
    if cmd[0] == "push":
        stack.push(int(cmd[1]))
    # 명령이 "pop"인 경우  
    elif cmd[0] == "pop":
        print(stack.pop())
    # 명령이 "size"인 경우
    elif cmd[0] == "size":
        print(stack.size())
    # 명령이 "empty"인 경우
    elif cmd[0] == "empty":
        print(stack.empty())
    # 명령이 "top"인 경우
    elif cmd[0] == "top":
        print(stack.top())