from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        count_dict = {}
        for i in range(n):
            if nums[i] in count_dict.keys():
                count_dict[nums[i]] += 1
            else:
                count_dict[nums[i]] = 1
        stack = PriorityQueue()
        for key in count_dict.keys():
            stack.put((count_dict[key], key))
            if stack.qsize() > k:
                stack.get()
        res = []
        while not stack.empty():
            res.append(stack.get()[1])
        res.reverse()
        return res