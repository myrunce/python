def compareArrays (arr1, arr2):
	if arr1 == arr2:
		print "The lists are the same."
	else:
		print "This lists are not the same."

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

list_three = ['celery','carrots','bread','milk']
list_four = ['celery','carrots','bread','cream']

compareArrays(list_one, list_two)
compareArrays(list_three, list_four)
