T = int(input())
print('test')
for _ in range(T):
    L, R, S = map(int, input().split())
    possible_steps = []

    # For L
    n = S - L
    if n >= 0 and isinstance(n, int):
        x = 2 * n + 1
        possible_steps.append(x)
    n = L - S - 1
    if n >= 0 and isinstance(n, int):
        x = 2 * n + 2
        possible_steps.append(x)

    # For R
    n = S - R
    if n >= 0 and isinstance(n, int):
        x = 2 * n + 1
        possible_steps.append(x)
    n = R - S - 1
    if n >= 0 and isinstance(n, int):
        x = 2 * n + 2
        possible_steps.append(x)

    if possible_steps:
        print(min(possible_steps))
    else:
        print(-1)
print('testtesttesttesttesttest')