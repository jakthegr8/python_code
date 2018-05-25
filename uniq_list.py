# Method 1
def uniq_list(nums):
  new_list = []
  for num in nums: 
  	if num not in new_list: 
  		new_list.append(num)
  return new_list

print(uniq_list([1, 1, 2, 2, 1, 7]))


# Method 2
def uniq_list2(nums):
  return list(set(nums))

print(uniq_list2([1, 1, 2, 2, 1, 7]))
