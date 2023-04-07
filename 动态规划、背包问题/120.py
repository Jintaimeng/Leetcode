class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        memo = [[None for _ in range(len(triangle[i]))] for i in range(len(triangle))]
        for i in range(len(triangle[-1])):
            memo[len(triangle) - 1][i] = triangle[-1][i]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                memo[i][j] = min((memo[i+1][j] + triangle[i][j]), (memo[i+1][j+1] + triangle[i][j]))
        return memo[0][0]