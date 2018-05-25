import string

def check_pangram(str, alp=string.ascii_lowercase):
	alp = set(alp)
	return alp <= set(str.lower())

print(check_pangram('The quick brown fox jumps over the lazy dog'))
print(check_pangram('The quick brown rat jumps over the lazy dog'))