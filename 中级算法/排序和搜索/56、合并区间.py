from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        res = []
        intervals = sorted(intervals)
        flag = intervals[0][1]
        begin = intervals[0][0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= flag:
                flag = max(intervals[i][1], flag)
            else:
                res.append([begin, flag])
                begin = intervals[i][0]
                flag = intervals[i][1]
        res.append([begin, flag])
        return res


def main():
    intervals = [[1,4],[4,5]]
    res = Solution().merge(intervals)
    print(res)


if __name__ == "__main__":
    main()