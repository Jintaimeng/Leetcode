class Solution:
    def strEncode(self, key, inputStr):
        visited = [False] * 26
        enlist = []
        for k in key:
            if not visited[ord(k) - ord('a')]:
                visited[ord(k) - ord('a')] = True
                enlist.append(k)

        for i in range(len(visited)):
            if not visited[i]:
                enlist.append(chr(ord('a') + i))
        res = ""
        for istr in inputStr:
            res += enlist[ord(istr) - ord('a')]
        return res

        
def main():
    print(Solution().strEncode(input(), input()))


if __name__ == "__main__":
    main()