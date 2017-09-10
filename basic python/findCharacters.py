def findChar (arr, letter):
	new_list = []
	letters = set(letter)
	for element in arr:
		if letters & set(element):
			new_list.append(element)
	print new_list
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
findChar(word_list, char)
			
		
