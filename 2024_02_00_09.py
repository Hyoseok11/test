def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    N = int(sys.stdin.readline())
    P = [0] * (N + 1)
    tmp = list(map(int, sys.stdin.readline().split()))
    for i in range(2, N + 1):
        P[i] = tmp[i - 2]

    A = list(map(int, sys.stdin.readline().split()))
    weights = [0] + A  # 1-indexed

    children = [[] for _ in range(N + 1)]
    parent = [0] * (N + 1)

    for u in range(2, N + 1):
        p = P[u]
        parent[u] = p
        children[p].append(u)

    alive = [True] * (N + 1)
    ans = []
    for _ in range(N):
        u = 1
        S = [u]
        ans.append(weights[1])
        while True:
            min_w = float('inf')
            min_c = None
            for c in children[u]:
                if alive[c] and weights[c] < min_w:
                    min_w = weights[c]
                    min_c = c
            if min_c is None:
                break
            u = min_c
            S.append(u)
        temp = weights[S[0]]
        for i in range(1, len(S)):
            weights[S[i - 1]] = weights[S[i]]
        weights[S[-1]] = temp
        leaf = S[-1]
        alive[leaf] = False
        p = parent[leaf]
        if p != 0:
            children[p].remove(leaf)

    for val in ans:
        print(val)

if __name__ == "__main__":
    main()
