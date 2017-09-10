sI = [1,2,3,4,5,6,7]
def filterType (variable):
	if isinstance(variable, int):
		if variable >= 100:
			print "That's a big number!"
		else:
			print "That's a small number."
	elif isinstance(variable, str):
		if len(variable) >= 50:
			print "Long sentence."
		else:
			print "Short sentence."
	if isinstance(variable, list):
		if len(variable) >= 10: 
			print "Big list!"
		else:
			print "Short list."
filterType(sI)
		
		
