def find_max(nums):
  if len(nums) <= 1:
    return nums[0]
  else:
    return nums[-1] if nums[-1] > find_max(nums[:-1]) else find_max(nums[:-1])
    
print(find_max([1, 9, 4, 25, 1]))