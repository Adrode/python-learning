def recursive_sum(nums):
  if len(nums) == 0:
    return 0
  else:
    return nums[-1] + recursive_sum(nums[:-1])
  
print(recursive_sum([1, 2, 3, 4, 20]))