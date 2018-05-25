# Method 1
def calc_case1(str):
	lc_count = 0
	uc_count = 0
	for char in str:
		if char == ' ': continue
		if char == char.upper():
			uc_count += 1
		else:
			lc_count += 1
	print(f'Total upper case chars: {uc_count}')
	print(f'Total lower case chars: {lc_count}')

calc_case1('Python Is Really Simple')

# Method 2
def calc_case2(str):
	lc_count = 0
	uc_count = 0
	for char in str:
		if char.isupper():
			uc_count += 1
		elif char.islower():
			lc_count += 1
	print(f'Total upper case chars: {uc_count}')
	print(f'Total lower case chars: {lc_count}')

calc_case2('Python Is Really Simple')  

