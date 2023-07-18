from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    row = len(matrix)
    col = len(matrix[0])
    row0 = [False] * row
    col0 = [False] * col
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                row0[i] = True
                col0[j] = True
    for i in range(row):
        if row0[i]:
            for c in range(col):
                matrix[i][c] = 0
    for j in range(col):
        if col0[j]:
            for r in range(row):
                matrix[r][j] = 0
    print(matrix)

def main():
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    setZeroes(matrix)

if __name__ == "__main__":
    main()