import random
def scoreGrade ():
	newArr = []
	x = 1
	while x <= 10:
		newArr.append(random.randint(60,100))
		x += 1
	print "Scores and Grades"
	for i in newArr:
		if i >= 90:
			print "Score: {}; Your grade is A.".format(i)
		elif i >= 80 and i < 90:
			print "Score: {}; Your grade is B.".format(i)
		elif i >= 70 and i < 80:
			print "Score: {}; Your grade is C.".format(i)
		elif i >= 60 and i < 70:
			print "Score: {}; Your grade is D.".format(i)
	print "End of program, Bye!"
			
scoreGrade()
