from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.word = word
        self.m = len(board)
        self.n = len(board[0])
        self.direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.used = [[False for _ in range(self.n)] for _ in range(self.m)]
        self.flag = False
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0]:
                    start_x = i
                    start_y = j
                    self.used[start_x][start_y] = True
                    self.getPath(board, start_x, start_y, 1)
                    if self.flag:
                        return True
                    else:
                        self.used = [[False for _ in range(self.n)] for _ in range(self.m)]
        return self.flag

    def getPath(self, board, x, y, start_word):
        if start_word == len(self.word):
            self.flag = True
            return
        for i in range(4):
            new_x = x + self.direction[i][0]
            new_y = y + self.direction[i][1]
            if new_x >= 0 and new_x < self.m and new_y >= 0 and new_y < self.n and not self.used[new_x][new_y] \
                and board[new_x][new_y] == self.word[start_word]:
                self.used[new_x][new_y] = True
                self.getPath(board, new_x, new_y, start_word + 1)
                self.used[new_x][new_y] = False







def main():
    board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    word = "ABCESEEEFS"
    res = Solution().exist(board, word)
    print(res)

if __name__ == "__main__":
    main()