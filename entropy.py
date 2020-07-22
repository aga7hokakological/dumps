import math
from collections import Counter

def entropy():
	string = str(input("Enter a string to calculate its entropy: "))
	list_string = list(Counter(string).values())
	print(list_string)
	arr = []

	for i in list_string:
		prob = (i/len(string))
		arr.append(- prob * math.log2(1/prob))
		entropy = - sum(arr)

	print(arr)
	print("The entropy of {} is : {}".format(string, entropy))

if __name__ == '__main__':
	entropy()