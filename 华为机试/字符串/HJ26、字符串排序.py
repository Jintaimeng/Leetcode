class Solution:
    def strSort(self):
        s = input()
        clear = ""
        for ss in s:
            if ss.isalpha():
                clear += ss
        new = sorted(clear, key=str.upper)
        res = ""
        index = 0
        for ss in s:
            if ss.isalpha():
                res += new[index]
                index += 1
            else:
                res += ss
        print(res)


def main():
    Solution().strSort()


if __name__ == "__main__":
    main()

