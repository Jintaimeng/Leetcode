from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:




def main():
    people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    res = Solution().reconstructQueue(people)
    print(res)

if __name__ == "__main__":
    main()