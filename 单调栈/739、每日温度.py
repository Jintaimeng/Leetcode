from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        deque = []
        deque.append(0)
        for i in range(1, len(temperatures)):
            while deque and temperatures[i] > temperatures[deque[-1]]:
                res[deque[-1]] = i - deque[-1]
                deque.pop()
            deque.append(i)
        return res


def main():
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    res = Solution().dailyTemperatures(temperatures)
    print(res)


if __name__ == "__main__":
    main()
