from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    res = []
    l = len(nums)
    nums.sort()
    for i in range(l):
        if nums[i] <= 0:
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L = i + 1
            R = l - 1
            while L < R:
                sum = nums[i] + nums[L] + nums[R]
                if sum == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L + 1]: L += 1
                    while L < R and nums[R] == nums[R - 1]: R -= 1
                    L += 1
                    R -= 1
                elif sum < 0:
                    L += 1
                elif sum > 0:
                    R -= 1
    return res

def main():
    nums = [-2,0,3,-1,4,0,3,4,1,1,1,-3,-5,4,0]
    res = threeSum(nums)
    print(res)

if __name__ == '__main__':
    main()