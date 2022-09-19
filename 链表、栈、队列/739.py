class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        answer = [0] * length
        stack = list()
        for i in range(length):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                answer[index] = i - index
            stack.append(i)
        return answer