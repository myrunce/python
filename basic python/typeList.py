def typeList(arr):
	if isinstance(arr, list):
			if all(isinstance(element, str) for element in arr):
				strSentence = ' '.join(arr)
				print "The array you entered is of the string type."
				print "string:", strSentence
			elif all(isinstance(element, int) or isinstance(element, float) for element in arr):
				totalSum = 0
				print "The array you entered is of the the integer type."
				for e in arr:
					totalSum += e
				print "Sum:", totalSum
			else:
				mixedSum = 0
				print "The array you entered is of the mixed type."
				int_list = [x for x in arr if isinstance(x, int) or isinstance(x, float)]
				for element in int_list:
					mixedSum += element
				str_list = [x for x in arr if isinstance(x, str)]
				mixedSentence = ' '.join(str_list)
				print "String:", mixedSentence
				print "Sum:", mixedSum
	else:
		print "Please enter a list"
typeList([19,98.99,77,1.2])
