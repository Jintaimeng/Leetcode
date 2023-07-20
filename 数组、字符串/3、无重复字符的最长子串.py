class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        if len(s) == 0:
            return res
        start_index = 0
        current_max = 1
        for index in range(1, len(s)):
            if s[index] not in s[start_index: index]:
                current_max += 1
            else:
                if current_max > res:
                    res = current_max
                start_index += s[start_index: index].find(s[index]) + 1
                current_max = index - start_index + 1
        if current_max > res:
            res = current_max
        return res


def main():
    s = "dvdf"
    res = Solution().lengthOfLongestSubstring(s)
    print(res)


if __name__ == "__main__":
    main()