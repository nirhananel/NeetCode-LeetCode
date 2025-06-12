class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      n = len(nums)
      esum= n * (n+1) // 2
      asum = sum(nums)
      return esum - asum