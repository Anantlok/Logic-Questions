class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        valid = 0
        
        for start in range(n):
            if nums[start] != 0:
                continue
            for direction in [1, -1]:  # 1 = right, -1 = left
                arr = nums[:]  # copy
                curr = start
                dir = direction
                
                while 0 <= curr < n:
                    if arr[curr] == 0:
                        curr += dir
                    else:
                        arr[curr] -= 1
                        dir = -dir  # reverse direction
                        curr += dir
                # check if all zero
                if all(x == 0 for x in arr):
                    valid += 1
        return valid
            