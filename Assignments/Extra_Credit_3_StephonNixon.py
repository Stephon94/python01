def centered_average(nums):
  nums.remove(max(nums))
  nums.remove(min(nums))
  
  avr = sum(nums)/len(nums)
  return avr
