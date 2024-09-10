class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
    

        left=0
        right=len (nums)-1
        while left<=right:
          mid=(left+right)//2
          if (nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]):
             return nums[mid]
          n=mid-1 if nums [mid-1]==nums [mid] else mid
          if n%2==1:
            right=mid-1
          else:
            left=mid+1

        
