my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def tuplesOut (var):
	myKeys = var.keys()
	myValues = var.values()
	newArr = []
	for x in range(0,len(myKeys)) and range(0,len(myValues)):
		myTuple = (myKeys[x],myValues[x])
		newArr.append(myTuple)
	return newArr
print tuplesOut(my_dict)
		
