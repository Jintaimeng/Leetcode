class Solution:
    def getWeight(self, n, weights, nums):
        sum = 0
        for i in range(n):
            sum += int(weights[i]) * int(nums[i])
        memo = [False] * (sum + 1)
        memo[0] = True
        for i in range(n):
            for j in range(int(nums[i])):
                for k in range(sum, -1, -1):
                    if k < int(weights[i]):
                        break
                    if memo[k - int(weights[i])]:
                        memo[k] = True
        res = 0
        for i in range(sum + 1):
            if memo[i]:
                res += 1
        return res


def main():
    n = int(input())
    weights = input().split(" ")
    nums = input().split(" ")
    print(Solution().getWeight(n, weights, nums))


if __name__ == "__main__":
    main()