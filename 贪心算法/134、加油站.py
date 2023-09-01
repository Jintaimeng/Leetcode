from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curSum = 0
        totalSum = 0
        start = 0
        for i in range(len(gas)):
            curSum += (gas[i] - cost[i])
            totalSum += (gas[i] - cost[i])
            if curSum < 0:
                start = i + 1
                curSum = 0
        if totalSum < 0:
            return -1
        return start


def main():
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    res = Solution().canCompleteCircuit(gas, cost)
    print(res)


if __name__ == "__main__":
    main()