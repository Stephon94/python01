# Extra Credit from CodingBat (http://codingbat.com/prob/p184853)

def big_diff(nums):
  smallest = 0
  largest = 0
  for number in nums:
    if number > largest:
      largest = number
      
    if smallest == 0:
      smallest = number
      
    if number < smallest:
      smallest = number
      
  return largest - smallest
