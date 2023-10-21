class Solution():
    def getCoor(self):
        coor = input().split(";")[: -1]
        x = 0
        y = 0
        for cr in coor:
            if self.isValid(cr):
                if cr[:1] == "A":
                    x -= int(cr[1:])
                elif cr[:1] == "D":
                    x += int(cr[1:])
                elif cr[:1] == "W":
                    y += int(cr[1:])
                elif cr[:1] == "S":
                    y -= int(cr[1:])
            else:
                continue
        print(x, y)

    def isValid(self, coor):
        if len(coor) > 0 and len(coor) <= 3:
            if coor[0] == "A" or coor[0] == "D" or coor[0] == "W" or coor[0] == "S":
                try:
                    if int(coor[1:]) > 0 and int(coor[1:]) < 100:
                        return True
                    else:
                        return False
                except:
                    return False
        return False


def main():
    Solution().getCoor()


if __name__ == "__main__":
    main()
