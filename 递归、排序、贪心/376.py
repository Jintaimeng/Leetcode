class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        beginState = 0
        upState = 1
        downState = 2
        res = 1
        state = beginState
        for i in range(1, len(nums)):
            if state == beginState:
                if nums[i-1] < nums[i]:
                    state = upState
                    res += 1
                elif nums[i-1] > nums[i]:
                    state = downState
                    res += 1
            elif state == upState:
                if nums[i - 1] > nums[i]:
                    state = downState
                    res += 1
            elif state == downState:
                if nums[i-1] < nums[i]:
                    state = upState
                    res += 1
        return res