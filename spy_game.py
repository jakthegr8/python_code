def spy_game(nums):
  spy_code = [0,0,7]
  for num in nums:
    if num == spy_code[0]:
    	spy_code.pop(0)
  return len(spy_code) == 0

print(spy_game([0, 1, 2, 0, 0, 7])) # True
print(spy_game([0, 1, 2, 0, 0])) # False