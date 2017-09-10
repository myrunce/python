name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def makeDict (arr1, arr2):
	if len(arr1) > len(arr2):
		newDict = zip(arr1, arr2)
		return newDict
	elif len(arr2) > len(arr1):
		newDict = zip(arr2, arr1)
		return newDict
	elif len(arr1) == len(arr2):
		newDict = zip(arr1, arr2)
		return newDict
		
print makeDict(name, favorite_animal)
	
