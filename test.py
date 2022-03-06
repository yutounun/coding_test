class Solution(object):
    def removeDuplicates(self, nums):
        i=0
        # nums[i+1]があるからnumの-1になってる
        # while i<len(nums)-1:
        #     if nums[i] == nums[i+1]:
        #         nums.pop(i)
        #     else:
        #         i += 1
        for i in range(len(nums)-2):
          if nums[i] == nums[i+1]:
                nums.pop(i)
        return len(nums)

test = Solution()
print(test.removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))