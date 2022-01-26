# 3. DFS & BFS
from collections import deque

def bfs(graph, start, visited):
    # 큐(Queue) 생성
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 첫번째 노드를 뽑아 출력
        v = queue.popleft()
        print(v, end = " ")
        # 해당 노드와 연결된 노드 방문
        for i in graph[v]:
            if not visited[i]:
                # 아직 방문하지 않은 노드일 경우 큐에 삽입
                queue.append(i)
                # 해당 노드 방문 처리
                visited[i] = True

def dfs(graph, node, visited):
    # 현재 노드를 방문 처리
    visited[node] = True
    # 방문 처리된 현재 노드 출력#
    print(node, end = " ")
    # 현재 노드와 연결된 다른 노드 방문
    for i in graph[node]:
        # 인접한 노드가 방문하지 않은 상태인 경우
        if not visited[i]:
            dfs(graph, i, visited)
    
# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],      # 1번 노드와 연결된 노드
    [1, 7],         # 2번 노드와 연결된 노드
    [1, 4, 5],      # 3번 노드와 연결된 노드
    [3, 5],         # 4번 노드와 연결된 노드
    [3, 4],         # 5번 노드와 연결된 노드
    [7],            # 6번 노드와 연결된 노드
    [2, 6, 8],      # 7번 노드와 연결된 노드
    [1, 7]          # 8번 노드와 연결된 노드
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 함수 호출
dfs(graph, 1, visited)
bfs(graph, 1, visited)