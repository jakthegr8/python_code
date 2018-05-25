def multiply_list(nums):
  total = 1
  for num in nums: total *= num
  return total

print(multiply_list([1, 2, 4, 1, 7]))
print(multiply_list([-3, 1, 2, 1, 4]))