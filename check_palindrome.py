# Method 1
def is_palindrome1(str):
  return str == str[::-1]

print(is_palindrome1('helleh')) # True
print(is_palindrome1('no poly')) # False

# Method 2
# Ugly way
def is_palindrome2(str):
  newstr = ''
  negIndex = (len(str) - 1) * -1
  for index in range(negIndex, 1): newstr += str[abs(index)]
  return str == newstr

print(is_palindrome2('helleh'))  # True
print(is_palindrome2('no poly')) # False

