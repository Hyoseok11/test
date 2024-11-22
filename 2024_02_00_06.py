
import sys
from collections import defaultdict, deque

def main():
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    boxes = []
    idx = 1
    for _ in range(N):
        A = int(data[idx])
        B = int(data[idx +1])
        boxes.append( (A, B) )
        idx +=2
    # N+1번째 상자는 비어있으므로 추가하지 않습니다.
    
    # 색깔별로 두 상자를 기록
    color_to_boxes = defaultdict(list)
    for box_idx, (A, B) in enumerate(boxes):
        if A != B:
            color_to_boxes[A].append(box_idx)
            color_to_boxes[B].append(box_idx)
        else:
            # 이미 정렬된 상자는 처리하지 않습니다.
            pass
    
    # 그래프 구축: 노드는 상자, 엣지는 같은 색깔을 가진 두 상자
    graph = defaultdict(list)
    for color, box_list in color_to_boxes.items():
        if len(box_list) !=2:
            # 각 색깔은 정확히 두 상자에만 있어야 합니다.
            print(-1)
            return
        u, v = box_list
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False]*N
    total_moves =0
    impossible = False
    
    for u in range(N):
        if not visited[u]:
            # 만약 이 상자가 이미 두 공이 같은 색깔이라면, 그래프에 포함되지 않으므로 건너뜁니다.
            A, B = boxes[u]
            if A == B:
                visited[u] = True
                continue
            # BFS를 통해 사이클의 길이를 계산합니다.
            queue = deque()
            queue.append((u, -1))
            visited[u] = True
            cycle_length =0
            is_cycle = True
            while queue:
                current, parent = queue.popleft()
                cycle_length +=1
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append((neighbor, current))
                    elif neighbor != parent:
                        # 사이클이 형성됨
                        pass
            # 모든 상자가 사이클을 이루므로, 사이클의 길이가 홀수인지 확인
            if cycle_length %2 ==0:
                print(-1)
                return
            total_moves += (cycle_length +1)
    
    print(total_moves)

if __name__ == "__main__":
    main()
