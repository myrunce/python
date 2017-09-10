students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

#part 1
def names (arr):
	for x in range(0,len(arr)):
		print arr[x]['first_name'], arr[x]['last_name']

names(students)

#part 2
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
	}

def names2 (var):
	print "Students"
	for x in range(0,len(var['Students'])):
		newArr = []
		newArr.append(var['Students'][x]['first_name'])
		newArr.append(var['Students'][x]['last_name'])
		temp = ''.join(newArr)
		nameLength = len(temp)
		print "{} - {} - {}".format(x+1, ' '.join(newArr), nameLength)
	print 'Instructors'
	for z in range(0,len(var['Instructors'])):
		newI = []
		newI.append(var['Instructors'][z]['first_name'])
		newI.append(var['Instructors'][z]['last_name'])
		tempI = ''.join(newI)
		nameLengthI = len(tempI)
		print "{} - {} - {}".format(z+1, ' '.join(newI), nameLengthI)
names2(users)
