def solve_xor_max(S):
    n = len(S)
    max_value = 0
    
    # 전체 문자열에서 가능한 최대의 XOR 값을 찾기 위해서
    # 모든 가능한 두 부분 문자열의 XOR 값을 계산한다.
    for i in range(n):
        for j in range(i, n):
            s1 = S[i:j+1]
            f_s1 = int(s1, 2)
            for k in range(n):
                for l in range(k, n):
                    s2 = S[k:l+1]
                    f_s2 = int(s2, 2)
                    max_value = max(max_value, f_s1 ^ f_s2)
    
    return bin(max_value)[2:]

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        S = data[index]
        index += 1
        
        result = solve_xor_max(S)
        results.append(result)
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
