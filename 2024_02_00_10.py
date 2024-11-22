from collections import defaultdict, deque

# 입력 데이터 수동 설정
def read_input():
    N = 6
    edges = [
        (1, 2, -1),
        (1, 3, 2),
        (2, 4, 2),
        (3, 5, -3),
        (3, 6, -1)
    ]
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    return N, graph

# BFS를 이용한 점수 및 초기화 횟수 계산
def bfs(start, graph, N):
    queue = deque([(start, 0)])  # (현재 노드, 현재 점수)
    visited = [False] * (N + 1)
    visited[start] = True
    total_scores = [0] * (N + 1)
    reset_counts = [0] * (N + 1)

    while queue:
        node, current_score = queue.popleft()
        for neighbor, weight in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                new_score = current_score + weight
                if new_score < 0:
                    reset_counts[neighbor] = reset_counts[node] + 1
                    new_score = 0
                else:
                    reset_counts[neighbor] = reset_counts[node]
                total_scores[neighbor] = total_scores[node] + max(new_score, 0)
                queue.append((neighbor, new_score))

    total_score = sum(total_scores)
    total_reset = sum(reset_counts)
    return total_score, total_reset

# 모든 시작 지점에 대해 결과 계산
def calculate_scores(N, graph):
    S = []
    C = []
    for i in range(1, N + 1):
        score, count = bfs(i, graph, N)
        S.append(score)
        C.append(count)
    return S, C

# 출력 처리
def print_result(S, C, calculate_C=True):
    if calculate_C:
        print(1)
        print(" ".join(map(str, S)))
        print(" ".join(map(str, C)))
    else:
        print(0)
        print(" ".join(map(str, S)))

# 메인 함수
def main():
    N, graph = read_input()
    S, C = calculate_scores(N, graph)
    print_result(S, C, calculate_C=True)

# 실행
main()
