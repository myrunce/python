def checkerboard ():
	x = 1 
	while x < 10:
		if x % 2 == 0:
			print "* * * *"
			x += 1
		else:
			print " * * * *"
			x += 1

checkerboard()
