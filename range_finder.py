# Method 1
def in_between(start, end, number):
	return start <= number <= end

print(in_between(1, 5, 3)) # True
print(in_between(0, 1, 2)) # False

# Method 2
def in_range(start, end, number):
	return number in range(start, end)

print(in_range(1, 5, 3)) # True
print(in_range(0, 1, 2)) # False

