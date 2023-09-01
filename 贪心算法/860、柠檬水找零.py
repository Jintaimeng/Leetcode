from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        map = {}
        for i in range(len(bills)):
            if bills[i] == 5:
                map[5] = map.get(5, 0) + 1
            elif bills[i] == 10:
                map[10] = map.get(10, 0) + 1
                if map.get(5, 0) == 0:
                    return False
                else:
                    map[5] -= 1
            elif bills[i] == 20:
                map[20] = map.get(20, 0) + 1
                if map.get(10, 0) > 0 and map.get(5, 0) > 0:
                    map[10] -= 1
                    map[5] -= 1
                elif map.get(5, 0) >= 3:
                    map[5] -= 3
                else:
                    return False
        return True


def main():
    bills = [5,5,5,10,20]
    res = Solution().lemonadeChange(bills)
    print(res)


if __name__ == "__main__":
    main()