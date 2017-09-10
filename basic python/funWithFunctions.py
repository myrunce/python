#odd/even
def oddEven ():
	x = 1
	while x <= 2000:
		if x % 2 != 0:
			print "Number is", x, "This is an odd number."
			x += 1
		else:
			print "Number is", x, "This is an even number."
			x += 1

#multiply
def multiply(arr, num):
	for x in range(0, len(arr)):
		arr[x] *= num
	return arr
	
a = [2,4,10,16]
b = multiply(a, 5)
print b
		
#hackerchallenge
def hackerChallenge(arr):
	print arr
	new_array = []
	for x in arr:
		val_arr = []
		for i in range(0,x):
			val_arr.append(1)
		new_array.append(val_arr)
	return new_array
		
print hackerChallenge(multiply(a, 5))
		
		
