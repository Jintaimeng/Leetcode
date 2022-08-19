class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = list()
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        res = [intervals[0][0], intervals[0][1]]
        for i in range(1, len(intervals)):
            if res[1] >= intervals[i][0] and res[1] < intervals[i][1]:
                res = [res[0], intervals[i][1]]
            elif res[1] < intervals[i][0]:
                result.append(res)
                res = [intervals[i][0], intervals[i][1]]
            if i == len(intervals) - 1:
                result.append(res)
        return result