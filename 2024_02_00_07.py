def count_v_cells(grid, n, m, start_row, start_col):
    count = 0
    # 왼쪽 위 대각선
    row, col = start_row, start_col
    while row >= 0 and col >= 0 and grid[row][col] == 1:
        count += 1
        row -= 1
        col -= 1
    # 오른쪽 위 대각선
    row, col = start_row - 1, start_col + 1
    while row >= 0 and col < m and grid[row][col] == 1:
        count += 1
        row -= 1
        col += 1
    return count

def apply_v_paint(grid, n, m, start_row, start_col):
    cells = []
    # 왼쪽 위 대각선
    row, col = start_row, start_col
    while row >= 0 and col >= 0 and grid[row][col] == 1:
        cells.append((row, col))
        row -= 1
        col -= 1
    # 오른쪽 위 대각선
    row, col = start_row - 1, start_col + 1
    while row >= 0 and col < m and grid[row][col] == 1:
        cells.append((row, col))
        row -= 1
        col += 1
    return cells

def max_blue_cells(grid, n, m):
    max_cells = 0
    first_v = []
    second_v = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                # 첫 번째 V자 색칠하기
                first_cells = apply_v_paint(grid, n, m, i, j)
                for row, col in first_cells:
                    grid[row][col] = 0  # 파란색으로 칠함
                # 두 번째 V자 색칠하기
                for x in range(n):
                    for y in range(m):
                        if grid[x][y] == 1:
                            second_count = count_v_cells(grid, n, m, x, y)
                            total_cells = len(first_cells) + second_count
                            if total_cells > max_cells:
                                max_cells = total_cells
                                first_v = list(first_cells)
                                second_v = apply_v_paint(grid, n, m, x, y)
                # 원래대로 복원
                for row, col in first_cells:
                    grid[row][col] = 1
    return max_cells

def main():
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, list(input().strip()))))
    result = max_blue_cells(grid, n, m)
    print(result)

if __name__ == "__main__":
    main()
