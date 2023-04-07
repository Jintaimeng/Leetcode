class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False
        if sum(matchsticks) % 4 != 0:
            return False
        self.matchsticks = sorted(matchsticks)
        self.bucket = [0, 0, 0, 0]
        self.length = sum(matchsticks) // 4
        return self.makesq(len(matchsticks) - 1)

    def makesq(self, index):
        if index <= -1:
            return True
        for i in range(len(self.bucket)):
            if self.bucket[i] + matchsticks[index] > self.length:
                continue
            self.bucket[i] += self.matchsticks[index]
            flag = self.makesq(index - 1)
            if flag:
                return True
            self.bucket[i] -= self.matchsticks[index]
        return False


