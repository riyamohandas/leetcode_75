class Solution:
    def findMin(self, nums: List[int]) -> int:
        big=max(nums)
        index=0
        for i in range(len(nums)):
            if nums[i]==big:
                index=i
                break
        result=nums[(index+1)%len(nums)]
        return result
