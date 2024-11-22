import sys
import bisect

def main():

    def solve():

        sys.setrecursionlimit(1 << 25)
        input = sys.stdin.read
        data = input().split()
        idx = 0
        L = int(data[idx]); idx +=1
        N = int(data[idx]); idx +=1
        K = int(data[idx]); idx +=1
        A = list(map(int, data[idx:idx+N]))
        A.sort()

        # Compute left_i and right_i for each Ai
        left = [0] * N
        right = [L] * N

        for i in range(N):
            if i > 0:
                left[i] = (A[i-1] + A[i]) // 2 +1
            else:
                left[i] = 0
            if i < N-1:
                right[i] = (A[i] + A[i+1]) // 2
            else:
                right[i] = L

        # Precompute list1 and list2
        list1 = [A[i] - left[i] for i in range(N)]
        list2 = [right[i] - A[i] for i in range(N)]
        list1_sorted = sorted(list1)
        list2_sorted = sorted(list2)

        # Function to compute union length for a given d
        def compute_union_length(d):
            total = 0
            current_start = max(0, A[0] - d)
            current_end = min(L, A[0] + d)
            for i in range(1, N):
                new_start = max(0, A[i] - d)
                new_end = min(L, A[i] + d)
                if new_start > current_end +1:
                    total += current_end - current_start +1
                    current_start = new_start
                    current_end = new_end
                else:
                    if new_end > current_end:
                        current_end = new_end
            total += current_end - current_start +1
            return total

        # Binary search to find d_max
        left_d = 0
        right_d = L
        while left_d < right_d:
            mid = (left_d + right_d) //2
            union = compute_union_length(mid)
            if union >= K:
                right_d = mid
            else:
                left_d = mid +1
        d_max = left_d

        result = []
        cumulative =0
        for d in range(0, d_max +1):
            # Count of Ai with list1 >= d
            count1 = N - bisect.bisect_left(list1_sorted, d)
            # Count of Ai with list2 >= d
            count2 = N - bisect.bisect_left(list2_sorted, d)
            if d ==0:
                freq = count1 + count2 - N
            else:
                freq = count1 + count2
            if cumulative + freq >= K:
                to_add = K - cumulative
                result.extend([d] * to_add)
                break
            else:
                result.extend([d] * freq)
                cumulative += freq
        print('\n'.join(map(str, result)))

    solve()

if __name__ == "__main__":
    main()
