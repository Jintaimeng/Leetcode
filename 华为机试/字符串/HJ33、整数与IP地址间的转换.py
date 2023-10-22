class Solution:
    def IPToInt(self, inputIp):
        ips = inputIp.split(".")
        ipstr = ""
        for ip in ips:
            ipstr += bin(int(ip))[2:].rjust(8, "0")
        return int("0b" + ipstr, 2)

    def IntToIP(self, inputInt):
        intStr = str(bin(int(inputInt))[2:]).rjust(32, "0")
        index = 0
        res = ""
        while index < len(intStr):
            res += str(int("0b" + intStr[index: index + 8], 2)) + "."
            index += 8
        return res[:-1]


def main():
    print(Solution().IPToInt(input()))
    print(Solution().IntToIP(input()))


if __name__ == "__main__":
    main()