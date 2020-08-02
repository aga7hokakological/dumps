def s_function(cnt: int):
	return cnt

def function_eq(n: int, m: int) -> int:
	n0 = s_function(n)
	# print(n0)
	if n + m == n0 + m:
		print(n0 + m)
		# print(s_function(n) + m)

def function(n: int) -> int:
	count = 0
	if n == 0:
		return count
	else:
		n-=1
		count+=1
	s_function(count)

def reflective(n: int, m: int) -> int:
	if n + 0 == 0 + n:
		return function_eq(n, m)

def natural_induction(n: int, m: int) -> int:
	if n + 0 == n:
		return reflective(n, m)

def first():
	n, m = map(int, input().split())
	return natural_induction(n, m)

def main():
	first()

if __name__ == '__main__':
	main()